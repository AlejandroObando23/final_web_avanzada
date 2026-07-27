from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prisma import Prisma
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Project CRUD API", port=3000)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prisma = Prisma()

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

# ==========================================
# Models for Validation
# ==========================================
class OrderItemCreate(BaseModel):
    product_id: str
    quantity: int
    unit_price: float

class OrderCreate(BaseModel):
    delivery_address: str
    notes: Optional[str] = None
    items: List[OrderItemCreate]
    total: float

# ==========================================
# Endpoints
# ==========================================
@app.get("/products")
async def get_products(search: Optional[str] = None):
    try:
        if search:
            products = await prisma.product.find_many(
                where={
                    'name': {
                        'contains': search
                    }
                }
            )
        else:
            products = await prisma.product.find_many()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/orders")
async def create_order(order: OrderCreate):
    try:
        # Create order and items in a transaction-like manner
        new_order = await prisma.order.create(
            data={
                'delivery_address': order.delivery_address,
                'notes': order.notes,
                'total': order.total,
                'status': 'pending',
                'items': {
                    'create': [
                        {
                            'productId': item.product_id,
                            'quantity': item.quantity,
                            'unit_price': item.unit_price
                        } for item in order.items
                    ]
                }
            }
        )
        return {"message": "Order created successfully", "order_id": new_order.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Seed some mock data for testing
@app.post("/seed")
async def seed_data():
    count = await prisma.product.count()
    if count == 0:
        await prisma.product.create_many(
            data=[
                {"name": "Bread", "description": "Freshly baked loaf", "price": 3.50, "stock": 20, "image_url": ""},
                {"name": "Milk", "description": "Whole milk gallon", "price": 4.99, "stock": 15, "image_url": ""},
                {"name": "Eggs", "description": "Dozen large eggs", "price": 2.99, "stock": 30, "image_url": ""},
                {"name": "Hair Wax", "description": "Strong hold matte wax", "price": 12.99, "stock": 50, "image_url": ""},
                {"name": "Beard Oil", "description": "Sandalwood scent", "price": 15.50, "stock": 10, "image_url": ""},
            ]
        )
        return {"message": "Database seeded with mock products."}
    return {"message": "Database already contains products."}

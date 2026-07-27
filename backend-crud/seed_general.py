import asyncio
from prisma import Prisma

async def main():
    prisma = Prisma()
    await prisma.connect()

    # Eliminar datos anteriores si se desea
    await prisma.product.delete_many()

    productos = [
        {
            "name": "Bread",
            "description": "Pan fresco recién horneado.",
            "price": 2.50,
            "stock": 50,
            "image_url": "https://example.com/bread.jpg"
        },
        {
            "name": "Milk",
            "description": "Leche entera fresca de granja.",
            "price": 3.20,
            "stock": 40,
            "image_url": "https://example.com/milk.jpg"
        },
        {
            "name": "Eggs",
            "description": "Docena de huevos de campo libres de jaula.",
            "price": 4.50,
            "stock": 30,
            "image_url": "https://example.com/eggs.jpg"
        },
        {
            "name": "Cheese",
            "description": "Queso cheddar maduro.",
            "price": 5.00,
            "stock": 25,
            "image_url": "https://example.com/cheese.jpg"
        }
    ]

    print("Insertando productos generales...")
    for p in productos:
        prod = await prisma.product.create(data=p)
        print(f"Producto creado: {prod.name} (ID: {prod.id})")

    print("Datos insertados correctamente.")
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())

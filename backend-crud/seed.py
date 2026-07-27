import asyncio
from prisma import Prisma

async def main():
    db = Prisma()
    await db.connect()

    products_data = [
        {
            "name": "Cera Mate PANDA",
            "description": "Cera fijadora de acabado mate para un look natural.",
            "price": 12.50,
            "stock": 50,
            "image_url": "https://example.com/cera.jpg"
        },
        {
            "name": "Aceite para Barba Premium",
            "description": "Aceite hidratante con esencia de sándalo.",
            "price": 18.00,
            "stock": 30,
            "image_url": "https://example.com/aceite.jpg"
        },
        {
            "name": "Shampoo Black & White",
            "description": "Shampoo especial para cuidado masculino.",
            "price": 15.00,
            "stock": 100,
            "image_url": "https://example.com/shampoo.jpg"
        }
    ]

    print("Insertando productos...")
    
    for p_data in products_data:
        # Create product
        product = await db.product.create(
            data=p_data
        )
        print(f"Producto creado: {product.name} (ID: {product.id})")

    await db.disconnect()
    print("Datos insertados correctamente.")

if __name__ == '__main__':
    asyncio.run(main())

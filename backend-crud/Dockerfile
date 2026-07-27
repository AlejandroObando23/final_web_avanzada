FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias necesarias para Prisma (openssl, etc)
RUN apt-get update && apt-get install -y openssl libatomic1 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Generar el cliente de Prisma
RUN prisma generate

EXPOSE 3000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]

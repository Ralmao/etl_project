# Usar una imagen oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt para instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de tu proyecto al contenedor
COPY . .

# Comando que ejecutará el script principal del ETL
CMD ["python", "main.py"]

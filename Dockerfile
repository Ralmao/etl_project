# Usa una imagen oficial de Python 3.10 como base
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el archivo main.py al contenedor
COPY main.py /app/

# Copia el código fuente (src) al contenedor
COPY src/ /app/src/

# Define las variables de entorno para las conexiones de base de datos
ENV ORIGEN_HOST=DB_HOST
ENV ORIGEN_PORT=5432
ENV ORIGEN_DB=DB_NAME
ENV ORIGEN_USER=DB_USER
ENV ORIGEN_PASSWORD=DB_PASSWORD

ENV DESTINO_HOST=DB_HOST
ENV DESTINO_PORT=5432
ENV DESTINO_DB=DB_NAME2
ENV DESTINO_USER=DB_USER
ENV DESTINO_PASSWORD=DB_PASSWORD

# Define el comando por defecto para ejecutar el script principal
CMD ["python", "main.py"]

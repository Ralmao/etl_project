from extract import extract_data
from transform import transform_data
from load import load_data
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Información de conexión a la base de datos de origen y destino
db_info_origen = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

db_info_destino = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME2')
}

# Consulta para la extracción de datos
query = "SELECT * FROM catalog.tb_cat_autopart LIMIT 10000"

# Proceso ETL
if __name__ == "__main__":
    # Extracción
    df = extract_data(db_info_origen, query)
    
    # Transformación
    df_clean = transform_data(df)
    
    # Carga
    load_data(df_clean, db_info_destino, 'transformed_autoparts')


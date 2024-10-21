from extract import extract_data
from transform import transform_data
from load import load_data

# Información de conexión a la base de datos de origen y destino
db_info_origen = {
    'host': '18.218.174.15',
    'user': 'querys',
    'password': '36690719',
    'database': 'db_dc'
}

db_info_destino = {
    'host': '18.218.174.15',
    'user': 'querys',
    'password': '36690719',
    'database': 'querys'
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

from sqlalchemy import create_engine
from .extract import get_connection_string  # Importar la función desde extract.py

def load_data(df, db_info, table_name):
    """Carga los datos transformados en la base de datos de destino."""
    connection_string = get_connection_string(db_info)
    engine = create_engine(connection_string)
    
    # Insertar los datos en la tabla destino
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Datos cargados exitosamente en la tabla {table_name}.")


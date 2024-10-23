import pandas as pd
from sqlalchemy import create_engine

def get_connection_string(db_info):
    """Construye la cadena de conexión a Postgres."""
    return f"postgresql://{db_info['user']}:{db_info['password']}@{db_info['host']}/{db_info['database']}"

def extract_data(db_info, query):
    """Extrae los datos de la base de datos origen."""
    connection_string = get_connection_string(db_info)
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df

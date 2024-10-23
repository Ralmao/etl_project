import pandas as pd
from sqlalchemy import create_engine

# Función para transformar el resultado de df.describe() a un formato tabular
def transform_describe_to_tabular(df):
    # Filtrar columnas numéricas para evitar problemas con tipos como Timestamp
    df_numeric = df.select_dtypes(include=['number'])
    
    # Obtener el resumen estadístico del DataFrame numérico
    df_desc = df_numeric.describe().T

    # Crear una nueva columna 'statistic' con los nombres de las estadísticas
    df_desc['statistic'] = df_desc.index

    # Reorganizar las columnas para que 'statistic' sea la primera
    cols = ['statistic'] + [col for col in df_desc.columns if col != 'statistic']
    df_desc = df_desc[cols]

    return df_desc

# Función para cargar el resumen de describe() a PostgreSQL
def load_describe_to_postgres(df_desc, db_info_destino):
    # Construir la cadena de conexión de PostgreSQL
    db_uri = f"postgresql://{db_info_destino['user']}:{db_info_destino['password']}@{db_info_destino['host']}/{db_info_destino['database']}"

    # Crear el motor de SQLAlchemy
    engine = create_engine(db_uri)
    
    # Cargar el DataFrame del resumen estadístico en PostgreSQL
    df_desc.to_sql('estadisticas_df_clean', engine, if_exists='replace', index=False)

# Función principal que procesa el describe() y lo carga a PostgreSQL
def process_describe_to_postgres(df_clean, db_info_destino):
    # Transformar el resumen estadístico del DataFrame limpio
    df_clean_desc = transform_describe_to_tabular(df_clean)
    
    # Cargar las estadísticas a PostgreSQL
    load_describe_to_postgres(df_clean_desc, db_info_destino)

    # Opcional: Devolver las estadísticas para revisión
    return df_clean_desc


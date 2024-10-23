import pandas as pd

# Transformación de los datos
def transform_data(df):
    # Eliminar columnas innecesarias
    df_drop = ['delete_date','update_date','year_to']
    
    df_clean = df.drop(df_drop, axis=1)

    # Rellenar valores por los mas cercanos y convertimos a enteros la columna year_from
    #df_clean['year_from'].fillna(method='bfill', inplace=True)
    df_clean['year_from'] = df_clean['year_from'].bfill()
    df_clean['year_from'] = df_clean['year_from'].astype(int)

    # Se sustituyen los valores faltantes por valores que no existen en las columnas en este caso se les da un valor de 0
    df_clean['id_cat_autopart_notes'] = df_clean['id_cat_autopart_notes'].fillna(0)
    df_clean['id_cat_autopart_engine_size'] = df_clean['id_cat_autopart_engine_size'].fillna(0)
    df_clean['id_cat_autopart_engine_type'] = df_clean['id_cat_autopart_engine_type'].fillna(0)
    df_clean['id_cat_autopart_model'] = df_clean['id_cat_autopart_model'].fillna(0)
    df_clean['id_cat_autopart_make'] = df_clean['id_cat_autopart_make'].fillna(0)

    # Convertir formatos de fecha de venezuela en caso de que sea necesario
    #df_clean['create_date'] = pd.to_datetime(df_clean['create_date']).dt.strftime('%Y-%m-%d %H:%M:%S')

    # Convertir a datetime
    df_clean['create_date'] = pd.to_datetime(df_clean['create_date'])

    return df_clean
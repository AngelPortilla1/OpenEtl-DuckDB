import polars as pl



def clean_raw_data(df: pl.DataFrame) -> pl.DataFrame:
    print("Iniciando limpieza de datos...")
    
    # Casteamos 'valor' a Float y las fechas a Datetime
    df_clean = df.with_columns([
        pl.col("valor").cast(pl.Float64),
        # Las fechas de Socrata suelen venir como "2023-12-01T00:00:00.000"
        pl.col("vigenciadesde").str.to_datetime("%Y-%m-%dT%H:%M:%S%.f").alias("fecha_inicio"),
        pl.col("vigenciahasta").str.to_datetime("%Y-%m-%dT%H:%M:%S%.f").alias("fecha_fin")
    ])
    
    # Opcional: podemos dropear las columnas originales de fecha si ya creamos alias limpios
    df_clean = df_clean.drop(["vigenciadesde", "vigenciahasta"])
    
    return df_clean

def apply_business_logic(df: pl.DataFrame) -> pl.DataFrame:
    """
    Crea métricas o agregaciones si es necesario.
    Por ejemplo: conteo de registros por municipio, o agrupar por especie/estado.
    """
    print("Aplicando reglas de negocio...")
    df_agg = df.group_by("columna_agrupacion").agg([
         pl.len().alias("total_registros")
     ])
    
    return df_agg

def run_transformations(df_raw: pl.DataFrame) -> pl.DataFrame:
    df_clean = clean_raw_data(df_raw)
    return df_clean

if __name__ == "__main__":
    # Aquí puedes hacer un mock rápido para probar
    df_mock = pl.DataFrame({"id": ["1", "2"], "name": ["A", None]})
    df_result = run_transformations(df_mock)
    print(df_result)
    pass
from src.extract import fetch_data_from_api
from src.transform import run_transformations
from src.load import load_to_duckdb

# URL del dataset (asumiendo que volviste al de la TRM que tiene 'vigenciadesde')
API_URL = "https://www.datos.gov.co/resource/32sa-8pi3.json"

def main():
    print("--- Iniciando Pipeline ETL ---")
    
    # FASE 1: Extracción
    print("\n1. Extracción")
    df_raw = fetch_data_from_api(API_URL, chunk_size=1000, max_records=2000)
    
    # Imprimimos las columnas reales extraídas del API ANTES de transformar
    print("Columnas disponibles desde la fuente:", df_raw.columns)
    
    # FASE 2: Transformación
    print("\n2. Transformación")
    # Pasamos el DataFrame REAL extraído del API, no el mock
    df_transformed = run_transformations(df_raw)
    
    print("\nEsquema final transformado:")
    print(df_transformed.schema)
    print(df_transformed.head(3))


    #Fase3 Carga
    print("\n3. Carga")
    load_to_duckdb(df_transformed, db_path="data/processed/warehouse.db")

    print("\n--- Pipeline ETL completado ---")

if __name__ == "__main__":
    main()
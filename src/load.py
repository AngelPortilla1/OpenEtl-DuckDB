import duckdb
import polars as pl
import os

def load_to_duckdb(df: pl.DataFrame, db_path: str = "data/processed/warehouse.db"):
    """
    Ingesta el DataFrame de Polars hacia una tabla física en DuckDB.
    """
    print(f"\nIniciando carga en base de datos: {db_path}")
    
    # Aseguramos que el directorio exista
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Conectamos a la base de datos local
    with duckdb.connect(db_path) as con:
        # DuckDB es capaz de leer la variable 'df' directamente desde el entorno de Python
        # Usamos CREATE OR REPLACE para ser idempotentes en este entorno de pruebas
        con.execute("""
            CREATE OR REPLACE TABLE trm_historico AS 
            SELECT * FROM df
        """)
        
        # Validación de integridad de la carga
        count = con.execute("SELECT COUNT(*) FROM trm_historico").fetchone()[0]
        print(f"Carga exitosa. Total de registros en la tabla 'trm_historico': {count}")

if __name__ == "__main__":
    pass
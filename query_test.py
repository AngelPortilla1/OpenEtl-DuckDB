import duckdb

def test_warehouse():
    db_path = "data/processed/warehouse.db"
    print(f"Conectando a {db_path}...")
    
    with duckdb.connect(db_path, read_only=True) as con:
        # Query analítico: Promedio anual de la TRM
        result = con.execute("""
            SELECT 
                EXTRACT(YEAR FROM fecha_inicio) AS anio,
                ROUND(AVG(valor), 2) AS promedio_trm,
                MAX(valor) AS trm_maxima
            FROM trm_historico
            WHERE fecha_inicio IS NOT NULL
            GROUP BY anio
            ORDER BY anio DESC
            LIMIT 5
        """).pl() # <-- Cambio clave: .pl() devuelve un DataFrame de Polars directamente
        
        print("\n--- Resultados Analíticos (Últimos 5 años) ---")
        print(result)

if __name__ == "__main__":
    test_warehouse()
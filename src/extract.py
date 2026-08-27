import requests
import polars as pl
from typing import List, Dict, Any

def fetch_data_from_api(url: str, chunk_size: int = 1000, max_records: int = 5000) -> pl.DataFrame:
    """
    Extrae datos paginados del API de Socrata usando offsets.
    """
    all_records: List[Dict[str, Any]] = []
    offset = 0
    
    print(f"Iniciando extracción desde: {url}")
    
    while True:
        params: Dict[str, Any] = {
            "$limit": chunk_size,
            "$offset": offset
        }
        
        try:
            response = requests.get(url, params=params, timeout=15)
            response.raise_for_status()
            
            chunk = response.json()
            if not chunk:
                break
                
            all_records.extend(chunk)
            offset += chunk_size
            
            if len(all_records) >= max_records:
                break
                
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión en el offset {offset}: {e}")
            raise
            
    return pl.DataFrame(all_records)
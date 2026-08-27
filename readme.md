# 📊 Open-Data ETL: Socrata API to DuckDB
[![Python](https://img.shields.io/badge/Python-3.12-36454F?style=for-the-badge&logo=python&logoColor=FFD700)](#)
[![Polars](https://img.shields.io/badge/Polars-Fast_DataFrames-00334E?style=for-the-badge&logo=polars&logoColor=white)](#)
[![DuckDB](https://img.shields.io/badge/DuckDB-In--Process_OLAP-FFD700?style=for-the-badge&logo=duckdb&logoColor=00334E)](#)
[![Data](https://img.shields.io/badge/Datos_Abiertos-Colombia-36454F?style=for-the-badge)](#)

## 📌 Visión General
Este proyecto implementa un pipeline ETL (Extract, Transform, Load) end-to-end diseñado para extraer volúmenes de datos gubernamentales desde la API de Datos Abiertos de Colombia (Socrata). 

El objetivo principal es demostrar un manejo eficiente de memoria y procesamiento analítico local implementando un flujo **Zero-Copy** entre Polars y DuckDB mediante Apache Arrow, eliminando los cuellos de botella tradicionales de Pandas.

## 🏗 Arquitectura del Pipeline

El sistema está desacoplado en módulos puros orquestados por un punto de entrada central, garantizando escalabilidad y fácil mantenimiento.

```mermaid
graph TD
    A[(API Datos Abiertos<br>Colombia / Socrata)] -->|Paginación chunk_size| B(Extracción: requests)
    B -->|JSON a Memoria| C(Transformación: Polars)
    C -->|Tipado Fuerte & Casteo| D{Apache Arrow<br>Zero-Copy}
    D -->|Ingesta In-Memory| E[(DuckDB<br>Warehouse Local)]
    E -->|Consultas SQL| F[Análisis Analítico]
    
    style A fill:#36454F,stroke:#FFD700,stroke-width:2px,color:#fff
    style B fill:#00334E,stroke:#fff,color:#fff
    style C fill:#00334E,stroke:#fff,color:#fff
    style D fill:#FFD700,stroke:#36454F,color:#36454F,stroke-width:2px
    style E fill:#36454F,stroke:#FFD700,stroke-width:2px,color:#fff
    style F fill:#00334E,stroke:#fff,color:#fff
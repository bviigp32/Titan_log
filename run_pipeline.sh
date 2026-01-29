#!/bin/bash

echo "========================================"
echo "TitanLog Data Pipeline Started..."
echo "========================================"

# 1. 데이터 생성
echo ">>> [1/3] Running Ingestion..."
python src/ingestion.py

# 2. 데이터 가공
echo ">>> [2/3] Running Processing (Spark ETL)..."
python src/processing.py

# 3. 데이터 분석
echo ">>> [3/3] Running Analytics..."
python src/analytics.py

echo "========================================"
echo "All Jobs Finished Successfully!"
echo "========================================"
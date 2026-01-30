# TitanLog: E-Commerce Log Analytics Lakehouse

> **"From Raw Logs to Business Insights"**
> 가상의 이커머스 로그 데이터를 수집, 정제, 분석, 시각화까지 수행하는 **End-to-End 데이터 레이크하우스** 프로젝트입니다.

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python) ![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5-E25A1C?logo=apachespark) ![MinIO](https://img.shields.io/badge/MinIO-Data%20Lake-C72C48?logo=minio) ![Docker](https://img.shields.io/badge/Docker-Cluster-2496ED?logo=docker)



## 프로젝트 성과 (Key Achievements)
* **대용량 처리 인프라 구축:** Docker Compose를 활용하여 Spark Cluster(Master/Worker)와 MinIO(S3) 데이터 레이크 환경을 **직접 구축**했습니다.
* **ETL 파이프라인 자동화:** `Ingestion(Bronze) -> Processing(Silver) -> Analytics(Gold)`로 이어지는 데이터 흐름을 Python 스크립트로 모듈화하고 쉘 스크립트로 **자동화**했습니다.
* **성능 최적화:** Partitioning과 Caching 전략을 적용하여 쿼리 조회 성능을 개선했습니다.
* **비즈니스 가치 창출:** Funnel 분석 및 트래픽 분석을 통해 데이터 기반의 의사결정을 지원하는 대시보드를 구현했습니다.

## 7-Day Challenge Log
* **Day 1:** Spark & MinIO Docker 인프라 구축
* **Day 2:** Faker를 이용한 데이터 수집기(Generator) 개발
* **Day 3:** PySpark 기반 ETL (JSON -> Parquet 변환)
* **Day 4:** 비즈니스 지표 분석 (Traffic, Ranking, Funnel)
* **Day 5:** 성능 튜닝 (Partitioning, Caching)
* **Day 6:** 파이프라인 자동화 (Shell Script)
* **Day 7:** 데이터 시각화 및 리포팅 (Matplotlib, Seaborn)

## 아키텍처 (Architecture)
| Layer | Role | Format | Key Logic |
| :--- | :--- | :--- | :--- |
| **Bronze** | Raw Data | JSON | 가상 로그 수집 (Ingestion) |
| **Silver** | Cleaned Data | Parquet | 스키마 적용, 결측치 제거, 파티셔닝 |
| **Gold** | Business Mart | Parquet | DAU 집계, 퍼널 분석, 랭킹 산출 |

## 실행 방법 (How to Run)
```bash
# 1. 인프라 실행
docker-compose up -d

# 2. 파이프라인 전체 실행 (수집->정제->분석)
./run_pipeline.sh

# 3. 시각화 확인
# Jupyter Lab 접속 -> 'visualization.ipynb' 실행

```

---

*Created by [Kim Kyunghun] during the 7-Day Data Challenge*


# TitanLog: 대용량 이커머스 로그 분석 레이크하우스

> **"하루 1GB씩 쌓이는 사용자 행동 데이터를 처리하라"**
> 가상의 이커머스 플랫폼에서 발생하는 대용량 로그(Clickstream)를 수집, 정제, 분석하는 **Spark 기반의 데이터 레이크하우스(Lakehouse)** 프로젝트입니다.

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python) ![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5-E25A1C?logo=apachespark) ![MinIO](https://img.shields.io/badge/MinIO-Data%20Lake-C72C48?logo=minio) ![Docker](https://img.shields.io/badge/Docker-Cluster-2496ED?logo=docker)

## 프로젝트 개요
현업 데이터 엔지니어링의 핵심 아키텍처인 **메달리온 구조(Medallion Architecture)**를 구현합니다.
Raw Data(Bronze)를 정제(Silver)하고, 비즈니스 지표로 가공(Gold)하는 전체 파이프라인을 **분산 처리 프레임워크(Spark)**로 구축합니다.

## 개발 로그 (2-Week Challenge)
* **Day 1: 데이터 센터 구축 (Infra Setup)**
  * Docker Compose를 활용한 Spark Cluster & MinIO & Jupyter 환경 구축
* **Day 2: 데이터 수집 (Ingestion - Bronze)**
  * `Faker` 가상 로그 생성 및 MinIO 적재 (JSON)
* **Day 3: 데이터 정제 (Transform - Silver)**
  * Spark ETL: Bronze(JSON) → Silver(Parquet) 변환
* **Day 4: 데이터 분석 (Analytics - Gold)**
  * 비즈니스 지표(Traffic, Ranking, Funnel) 도출 및 Mart 적재
* **Day 5: 성능 최적화 (Performance Tuning)**
  * **Partitioning:** `event_type` 컬럼 기준 물리적 파티셔닝 적용 (Scan 성능 향상)
  * **Caching:** 반복 사용되는 DataFrame에 `.cache()` 적용하여 In-Memory 처리 속도 개선
* **Day 6: 파이프라인 자동화 (Automation)**
  * Notebook 코드를 모듈화하여 `.py` 스크립트로 변환 (`src/` 폴더)
  * `run_pipeline.sh` 쉘 스크립트로 전체 ETL 과정(Ingestion -> Processing -> Analytics) 원클릭 실행 구현

## 아키텍처 (Architecture)
1.  **Ingestion (Bronze):** Raw JSON
2.  **Processing (Silver):** Parquet + Partitioning
3.  **Analytics (Gold):** Data Mart
4.  **Storage:** MinIO (Data Lake)

## 기술 스택 (Tech Stack)
| Category | Technology | Usage |
| :--- | :--- | :--- |
| **Language** | Python 3.9+ | 전체 로직 구현 |
| **Processing** | **Apache Spark** | 대용량 분산 처리 & ETL |
| **Storage** | **MinIO (S3)** | Data Lake (Bronze/Silver/Gold) |
| **Format** | Parquet, JSON | 데이터 저장 포맷 |
| **DevOps** | Docker | 인프라 오케스트레이션 |

## 실행 방법 (How to Run)
```bash
# 1. 인프라 실행
docker-compose up -d

# 2. 파이프라인 실행 (Jupyter Lab)
# - data_generator.ipynb (생성)
# - bronze_to_silver.ipynb (정제)
# - silver_to_gold.ipynb (분석)
# - optimization.ipynb (최적화 실험)

# 전체 파이프라인 자동 실행
./run_pipeline.sh

```

---

*Created by [Kim Kyunghun]*


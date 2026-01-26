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
  * `Faker`를 활용한 가상 로그 생성기 구현 및 MinIO 적재 (JSON)
  * 파티셔닝 전략 적용 (`log_date=YYYY-MM-DD`)
* **Day 3: 데이터 정제 (Transform - Silver)**
  * **PySpark**와 **MinIO(S3)** 연동 환경 구성 (Hadoop AWS Jars)
  * **ETL 파이프라인 1단계:** Bronze(JSON) → Silver(Parquet) 변환
  * 스키마(Schema) 정의 및 결측치 제거, 컬럼 최적화 수행

## 아키텍처 (Architecture)
1.  **Ingestion (Bronze):** Python Generator가 생성한 Raw JSON 로그 적재
2.  **Processing (Silver):** PySpark를 통해 데이터 타입 변환 및 Parquet 포맷으로 압축 저장
3.  **Analytics (Gold):** *(Coming Soon)* 비즈니스 지표 집계 및 분석
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

# 2. 데이터 생성 (Bronze 적재)
# Jupyter Lab 접속 -> 'data_generator.ipynb' 실행

# 3. 데이터 정제 (Silver 변환)
# Jupyter Lab 접속 -> 'bronze_to_silver.ipynb' 실행
# -> MinIO 'silver' 버킷에 Parquet 파일 생성 확인

```

---

*Created by [Kim Kyunghun]*


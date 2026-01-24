# TitanLog: 대용량 이커머스 로그 분석 레이크하우스

> **"하루 1GB씩 쌓이는 사용자 행동 데이터를 처리하라"**
> 가상의 이커머스 플랫폼에서 발생하는 대용량 로그(Clickstream)를 수집, 정제, 분석하는 **Spark 기반의 데이터 레이크하우스(Lakehouse)** 프로젝트입니다.

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python) ![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5-E25A1C?logo=apachespark) ![MinIO](https://img.shields.io/badge/MinIO-Data%20Lake-C72C48?logo=minio) ![Docker](https://img.shields.io/badge/Docker-Cluster-2496ED?logo=docker)

## 프로젝트 개요
현업 데이터 엔지니어링의 핵심 아키텍처인 **메달리온 구조(Medallion Architecture)**를 구현합니다.
Raw Data(Bronze)를 정제(Silver)하고, 비즈니스 지표로 가공(Gold)하는 전체 파이프라인을 **분산 처리 프레임워크(Spark)**로 구축합니다.



## 개발 로그 (2-Week Challenge)
* **Day 1: 데이터 센터 구축 (Infra Setup)**
  * Docker Compose를 활용한 **Spark Cluster** (Master x1, Worker x1) 구축
  * S3 호환 Object Storage인 **MinIO** 구축 및 버킷 생성 (`bronze`, `silver`, `gold`)
  * PySpark 개발을 위한 **Jupyter Lab** 환경 연동

## 아키텍처 (Architecture)
* **Ingestion:** Python Faker (Log Generator) -> MinIO (Bronze)
* **Processing:** Apache Spark (PySpark)
  * **Bronze:** Raw JSON 데이터 적재
  * **Silver:** Parquet 변환, 결측치 처리, 스키마 적용
  * **Gold:** 일별 집계, Funnel 분석, User Session 분석
* **Storage:** MinIO (Data Lake)
* **Environment:** Docker Container

## 기술 스택 (Tech Stack)
| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **Processing** | **Apache Spark (PySpark)** |
| **Storage** | **MinIO (S3 Compatible)** |
| **Format** | Parquet, JSON |
| **DevOps** | Docker, Docker Compose |

## 실행 방법 (How to Run)
```bash
# 1. 인프라 실행 (Spark Cluster & MinIO)
docker-compose up -d

# 2. 상태 확인
# Spark Master: http://localhost:8080
# MinIO Console: http://localhost:9001
# Jupyter Lab: http://localhost:8888

```

---

*Created by [Kim Kyunghun]*


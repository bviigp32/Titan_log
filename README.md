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
  * MinIO 버킷 생성 (`bronze`, `silver`, `gold`)
* **Day 2: 데이터 수집기 구현 (Data Ingestion)**
  * `Faker` 라이브러리를 활용한 가상 이커머스 로그 생성기(Generator) 개발
  * MinIO `bronze` 버킷에 JSON 포맷으로 파티셔닝(`log_date=YYYY-MM-DD`) 적재 구현

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
| **Library** | Faker, MinIO Client |
| **DevOps** | Docker, Docker Compose |

## 실행 방법 (How to Run)
```bash
# 1. 인프라 실행
docker-compose up -d

# 2. 데이터 생성 (Data Generator)
# Jupyter Lab(http://localhost:8888)에 접속하여 'data_generator.ipynb' 실행
# -> MinIO 'bronze' 버킷에 가짜 로그 데이터가 적재됨.

```

---

*Created by [Kim Kyunghun]*



### 💾 Git Commit (Day 2 마무리)

잠깐! 커밋하기 전에 Jupyter Lab에서 작성한 코드를 저장해야 합니다.
1.  Jupyter Lab에서 파일 이름을 `Untitled.ipynb` → **`data_generator.ipynb`**로 변경해주세요. (우클릭 -> Rename)
2.  `Ctrl + S` (저장)

그다음 터미널에서 아래 명령어를 실행하세요.

```bash
# 1. 변경된 파일(README, 노트북) 담기
git add .

# 2. 커밋 메시지 작성
git commit -m "feat: Day 2 - Implement Fake Log Generator and Ingestion to MinIO"

# 3. 푸시 (선택사항)
# git push

```

---

### 📅 Day 3 예고: "PySpark 시동 걸기"

지금 MinIO에는 `JSON` 형태의 날것 그대로의 데이터(Bronze)가 쌓여있습니다.
내일은 **Apache Spark**를 사용해서 이 데이터를 읽어 들이고, 분석하기 좋게 다듬어서 **Silver(Parquet)** 영역으로 옮기는 **ETL의 꽃, Transform** 과정을 시작해 보겠습니다.

오늘도 정말 고생 많으셨습니다! 푹 쉬세요! 🦁👍
# src/processing.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

def run():
    print("[Step 2] Processing: Bronze -> Silver 변환 시작...")
    
    spark = SparkSession.builder \
        .appName("TitanLog-Processing") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.533") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://titan-minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    # 읽기 & 변환
    bronze_df = spark.read.json("s3a://bronze/*/*.json")
    silver_df = bronze_df \
        .withColumn("event_time", to_timestamp(col("timestamp"))) \
        .drop("timestamp") \
        .dropna(subset=["user_id", "item_id"])

    # 파티셔닝 저장
    silver_df.write.mode("overwrite").partitionBy("event_type").parquet("s3a://silver/log_partitioned")
    print("Processing 완료 (Silver 저장됨)")
    spark.stop()

if __name__ == "__main__":
    run()
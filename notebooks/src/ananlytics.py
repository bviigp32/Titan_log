# src/analytics.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, count, desc

def run():
    print("[Step 3] Analytics: Silver -> Gold 분석 시작...")
    
    spark = SparkSession.builder \
        .appName("TitanLog-Analytics") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.533") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://titan-minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    df = spark.read.parquet("s3a://silver/log_partitioned")

    # 간단하게 베스트셀러 분석만 수행 (시간 관계상)
    top_sellers = df.filter(col("event_type") == "purchase") \
        .groupBy("item_id").count().orderBy(desc("count"))
    
    top_sellers.write.mode("overwrite").parquet("s3a://gold/top_selling_items")
    top_sellers.show(5)
    
    print("Analytics 완료 (Gold 저장됨)")
    spark.stop()

if __name__ == "__main__":
    run()
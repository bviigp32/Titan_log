# src/ingestion.py
import json
import time
import random
import io
from datetime import datetime
from faker import Faker
from minio import Minio

# 설정
MINIO_ENDPOINT = "titan-minio:9000"
ACCESS_KEY = "minioadmin"
SECRET_KEY = "minioadmin"
BUCKET_NAME = "bronze"

def run():
    fake = Faker()
    client = Minio(MINIO_ENDPOINT, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
    
    if not client.bucket_exists(BUCKET_NAME):
        client.make_bucket(BUCKET_NAME)
        
    print("[Step 1] Ingestion: 가짜 로그 데이터 생성 시작...")
    
    # 5개의 파일 생성 (총 5000건)
    for i in range(5):
        logs = []
        for _ in range(1000):
            event_type = random.choices(['view', 'cart', 'purchase'], weights=[0.7, 0.2, 0.1])[0]
            log = {
                "event_id": fake.uuid4(),
                "user_id": random.randint(1000, 1100),
                "item_id": random.randint(1, 50),
                "event_type": event_type,
                "timestamp": datetime.now().isoformat(),
                "device_os": random.choice(['Android', 'iOS', 'Web']),
                "ip_address": fake.ipv4()
            }
            logs.append(log)
            
        data_bytes = json.dumps(logs).encode('utf-8')
        file_name = f"log_date={datetime.now().strftime('%Y-%m-%d')}/log_{datetime.now().strftime('%H%M%S')}_{i}.json"
        
        client.put_object(BUCKET_NAME, file_name, io.BytesIO(data_bytes), len(data_bytes), content_type='application/json')
        print(f"   - Uploaded: {file_name}")
        time.sleep(0.5)

    print("Ingestion 완료!")

if __name__ == "__main__":
    run()
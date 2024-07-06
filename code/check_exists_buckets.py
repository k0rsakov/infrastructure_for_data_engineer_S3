from minio import Minio

# Импорт из локальной переменной секретных данных
from cred import s3_minio_access_key, s3_minio_secret_key

# Не меняется, это единый endpoint для подключения к S3
endpoint = 'localhost:9000'
# access key для подключения к бакету
access_key = s3_minio_access_key
# secret key для подключения к бакету
secret_key = s3_minio_secret_key

client = Minio(
    endpoint=endpoint,
    access_key=access_key,
    secret_key=secret_key,
    secure=False,  # https://github.com/minio/minio/issues/8161#issuecomment-631120560
)

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

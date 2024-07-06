import pandas as pd

# Импорт из локальной переменной секретных данных
from cred import s3_minio_access_key, s3_minio_secret_key

bucket_name = 'test-local-bucket'
file_name = 'titanic.csv'

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

df.to_csv(
    path_or_buf=f's3://{bucket_name}/{file_name}',
    index=False,
    escapechar='\\',
    compression='gzip',
    storage_options={
        "key": s3_minio_access_key,
        "secret": s3_minio_secret_key,
        # https://github.com/mlflow/mlflow/issues/1990#issuecomment-659914180
        "client_kwargs": {"endpoint_url": "http://localhost:9000"},
    },
)

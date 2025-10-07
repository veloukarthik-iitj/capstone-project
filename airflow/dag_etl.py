"""Example Airflow DAG to run the ETL on a schedule. Adjust connection IDs and paths for your environment."""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='diabetes_etl',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    default_args={'retries': 1, 'retry_delay': timedelta(minutes=5)}
) as dag:

    ingest = BashOperator(
        task_id='ingest_csv',
        bash_command='python /opt/airflow/dags/../src/ingest.py --input /opt/airflow/data/diabetic_data.csv --output /opt/airflow/data/tmp/diabetic.parquet'
    )

    clean = BashOperator(
        task_id='clean_data',
        bash_command='python /opt/airflow/dags/../src/clean.py --input /opt/airflow/data/tmp/diabetic.parquet --output /opt/airflow/data/cleaned/diabetic_clean.parquet'
    )

    ingest >> clean

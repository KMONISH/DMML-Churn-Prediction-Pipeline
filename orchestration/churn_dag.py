from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(dag_id='churn_pipeline_demo', start_date=datetime(2025,1,1), schedule_interval='@daily', catchup=False) as dag:
    ingest = BashOperator(task_id='ingest', bash_command='python ingestion/ingest_csv.py')
    validate = BashOperator(task_id='validate', bash_command='python validation/validate_data.py')
    prepare = BashOperator(task_id='prepare', bash_command='python preparation/prepare_data.py')
    train = BashOperator(task_id='train', bash_command='python training/train.py')
    score = BashOperator(task_id='score', bash_command='python scoring/score_batch.py')

    ingest >> validate >> prepare >> train >> score

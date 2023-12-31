from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'fable',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
    'start_date' : datetime(2023,12,30),
    'schedule_interval' : '@daily'
    
    }

with DAG(dag_id='dag_with_catchup_and_backfill', 
         default_args=default_args,
         catchup=True) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo this is a simle bash command'
    )
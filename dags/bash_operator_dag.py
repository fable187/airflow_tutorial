from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'fable',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
with DAG(
    
    dag_id = "bash_operator_dag_v3",
    description="This is our bash operator dag",
    start_date=datetime(2023,12,30),
    schedule_interval='@daily'
    ) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo this is the first task"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo this is the second task!"
    )
    
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo this is the third task running with task two!"
    )
    
    task1 >> [task2, task3]
    
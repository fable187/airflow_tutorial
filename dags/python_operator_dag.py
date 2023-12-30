from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.models.taskinstance import TaskInstance

def greet(ti: TaskInstance):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    

    print(f'Hello {first_name} {last_name}!')
    
def get_name(ti: TaskInstance):
    ti.xcom_push(key='first_name', value = 'Jerry')
    
    ti.xcom_push(key='last_name', value='Fridman')
    
def get_age(ti: TaskInstance):
    ti.xcom_push(key='age', value=19)
    

default_args = {
    'owner': 'fable',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
    'start_date' : datetime(2023,12,30),
    'schedule_interval' : '@daily'
    
    }

with DAG(
    default_args=default_args,
    dag_id="python_dag_v6",
    description="This is a dag running a python script",
    
) as dag:
    get_name_task = PythonOperator(
        task_id='get_name',
        python_callable=get_name
        
    )
    greet_task = PythonOperator(
        task_id='greet',
        python_callable=greet
        
    )
    
    get_age_task = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    
    [get_name_task , get_age_task] >> greet_task
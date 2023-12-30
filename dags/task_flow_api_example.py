from airflow.decorators import dag, task 
from datetime import datetime, timedelta

default_args = {
    'owner': 'fable',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
    'start_date' : datetime(2023,12,30),
    'schedule_interval' : '@daily'
    
    }

@dag(dag_id='dag_with_task_flow_api_v1',
     default_args=default_args,
     )
def hello_world_etl():
    
    @task()
    def get_name():
        return 'Jerry'
    
    @task()
    def get_age():
        return 19
    
    @task()
    def greet(name, age):
        print(f"Hello world! my name is: {name} and I am {age} years old!")
        
    name = get_name()
    age = get_age()
    greet(name=name, age=age)
    
greet_dag = hello_world_etl()
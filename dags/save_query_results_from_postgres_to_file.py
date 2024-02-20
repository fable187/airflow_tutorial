from airflow.decorators import dag, task 
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd

default_args = {
    'owner': 'fable',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
    'start_date' : datetime(2023,12,30),
    'schedule_interval' : '@daily'
    
    }

@dag(dag_id='query_postgres_and_save_to_file_dag',
     default_args=default_args,
     )
def syphon_info():
    
    @task()
    def retrieve_data():
        # import pudb;pudb.set_trace()
        hook = PostgresHook(postgres_conn_id='airflow_postgress')
        with hook.get_conn() as conn:
            dag_run_df = pd.read_sql(con=conn, sql="select * from dag_run")
            dag_run_df.to_csv("dag_runs.csv")
         
    retrieve_data()
    
syphon_info()



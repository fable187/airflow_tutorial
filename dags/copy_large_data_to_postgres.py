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

@dag(dag_id='transfer_big_data',
     default_args=default_args,
     )
def syphon_info():
    
    @task()
    def get_sql_data():
        import sqlite3
        conn = sqlite3.connect('/opt/airflow/dags/generated_data.db')
        data_df = pd.read_sql( "select * from my_table", con=conn)
        return data_df
    
    # @task()
    # def retrieve_data(results_df:pd.DataFrame):
    #     # import pudb;pudb.set_trace()
    #     hook = PostgresHook(postgres_conn_id='airflow_postgress')
    #     with hook.get_conn() as conn:
    #         results_df.to_sql(conn)
         
    get_sql_data()
    
syphon_info()
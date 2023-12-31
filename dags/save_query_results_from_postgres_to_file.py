from airflow.decorators import dag, task 
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import csv
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
        conn = hook.get_conn()
        cursor = conn.cursor()
        cursor.execute("select * from dag_run")
        with open("dag_runs.txt", "w") as w:
            csv_writer = csv.writer(w)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)
        cursor.close()
        conn.close()
        
        
    retrieve_data()
    
syphon_info()
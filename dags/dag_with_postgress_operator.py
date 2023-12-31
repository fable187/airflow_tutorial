from airflow import DAG 
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'fable',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id = 'dag_with_postgres_operator_v01',
    default_args=default_args,
    start_date=datetime(2023,12,30),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='airflow_postgress',
        sql="""
            create table if not exists my_dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )
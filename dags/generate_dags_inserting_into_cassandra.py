# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime, timedelta
# import pandas as pd
# from sqlalchemy import create_engine
# # from cassandra.cluster import Cluster

# def generate_dag(dag_id, schedule_interval, dag_number):
#     default_args = {
#         'owner': 'airflow',
#         'start_date': datetime(2023, 1, 1),
#         'depends_on_past': False,
#         'retries': 1,
#         'retry_delay': timedelta(minutes=5),
#     }

#     dag = DAG(
#         dag_id=dag_id,
#         default_args=default_args,
#         schedule_interval=schedule_interval,
#     )

#     def task1_callable(**kwargs):
#         # This function represents Task 1
#         df = pd.DataFrame({'dag_number': [dag_number], 'message': ['Hello from Task 1']})

#         # Store DataFrame in SQLite database
#         engine = create_engine('sqlite:///airflow_example.db')
#         df.to_sql(f'dag_{dag_number}_data', con=engine, index=False, if_exists='replace')

#     def task2_callable(**kwargs):
#         # This function represents Task 2
#         dag_number = kwargs['dag_run'].conf['dag_number']

#         # Retrieve DataFrame from SQLite database
#         engine_sqlite = create_engine('sqlite:///airflow_example.db')
#         df = pd.read_sql(f'select * from dag_{dag_number}_data', con=engine_sqlite)

#         # Store DataFrame in Cassandra database
#         cluster = Cluster(['your_cassandra_host'])
#         session = cluster.connect('your_keyspace')

#         # Assuming your_table is the table where you want to store the DataFrame
#         session.execute(f"INSERT INTO your_table (dag_number, message) VALUES ({dag_number}, '{df.iloc[0]['message']}')")

#     with dag:
#         # Define PythonOperators as tasks
#         task1 = PythonOperator(
#             task_id='task1',
#             python_callable=task1_callable,
#             provide_context=True,
#         )

#         task2 = PythonOperator(
#             task_id='task2',
#             python_callable=task2_callable,
#             provide_context=True,
#         )

#         # Set up the task dependencies
#         task1 >> task2

#     return

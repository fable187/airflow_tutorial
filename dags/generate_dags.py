from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def generate_dag(dag_id, schedule_interval, dag_number):
    default_args = {
        'owner': 'airflow',
        'start_date': datetime(2023, 1, 1),
        'depends_on_past': False,
        'retries': 5,
        'retry_delay': timedelta(minutes=5),
    }

    dag = DAG(
        dag_id=dag_id,
        default_args=default_args,
        schedule_interval=schedule_interval,
    )

    with dag:
        # Define a BashOperator task to print the message
        task_hello = BashOperator(
            task_id=f'print_hello',
            bash_command=f'echo "Hello there from dag {dag_number}"'
        )
        
        
    return dag

# Define the number of DAGs you want to generate
num_dags = 5

# Iterate and generate DAGs
for i in range(num_dags):
    dag_id = f'dynamic_dag_{i}'
    schedule_interval = timedelta(days=1)  # You can customize the schedule interval

    # Generate DAG dynamically
    globals()[dag_id] = generate_dag(dag_id, schedule_interval, i)

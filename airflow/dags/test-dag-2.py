from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'lucastercas',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(
    'test-dag-2',
    default_args=default_args,
    description='A test DAG',
    schedule_interval='*/1 * * * *',
    #catchup=True
)

t1 = BashOperator(
    task_id='test-dag-date-2',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='test-dag-echo',
    bash_command='echo foo',
    retries=3,
    dag=dag
)

t1 >> t2

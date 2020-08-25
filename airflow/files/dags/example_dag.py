from datetime import datetime, timedelta

from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
  'owner': 'lucastercas',
  'depends_on_past': False,
  'catchup': False,
  'start_date': days_ago(2),
  'retries': 2,
  'retry_delay': timedelta(minutes=2),
}

dag = DAG(
  'example_dag',
  default_args=default_args,
  description='A test DAG',
  schedule_interval='0 1 * * *'
)

with dag:
  t1 = BashOperator(
    task_id='example_operator_date',
    bash_command='date'
  )

  t2 = BashOperator(
    task_id='example_operator_bash',
    bash_command='echo bar',
    retries=3
  )

  t1 >> t2

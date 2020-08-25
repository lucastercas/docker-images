from datetime import datetime, timedelta
from airflow import DAG

from operators.freetds_operator import FreeTDSOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'lucastercas',
    'depends_on_past': False,
    'catchup': False,
    'start_date': days_ago(2),
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
    'description': f'Example FreeTDS MsSQL DAG'
}

dag = DAG(
    dag_id="example_freetds",
    default_args=default_args,
    schedule_interval="*/2 * * * *"
)

with dag:
    date = datetime.now().strftime("%Y-%m-%d")
    server = "mssql-server"
    port = "1433"
    user = "SA"
    pwd = "t3st_Password"

    step_1 = FreeTDSOperator(
        task_id="example_freetds_operator",
        sql=f"SET NOCOUNT ON; EXEC test_proc_2",
        conn={
            'server': server,
            'port': port,
            'user': user,
            'pwd': pwd
        }
    )

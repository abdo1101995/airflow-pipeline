from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime ,timedelta
def my_func():
    print('Hello from my_func')
def start_func() :
    print("hello to airflow")

with DAG('thee_dag', description='Python DAG', schedule_interval='*/5 * * * *', start_date=datetime(2018, 11, 1), catchup=False) as dag:
    dummy_task 	= PythonOperator(task_id='dummy_task', python_callable=start_func,retries=10,retry_delay=timedelta(seconds=1))
    python_task	= PythonOperator(task_id='python_task', python_callable=my_func)
    dummy_task >> python_task
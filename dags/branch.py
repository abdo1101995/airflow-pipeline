from airflow.models import DAG
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

dag = DAG('BranchingTest', default_args={'start_date': datetime(2020, 4, 15)}, schedule_interval='@daily')

def branch_test(**kwargs):
  if int(kwargs['ds_nodash']) % 2 == 0:
    return 'even_day_task'
  else:
    return 'odd_day_task'
 
start_task = DummyOperator(task_id='start_task', dag=dag)

branch_task = BranchPythonOperator(
       task_id='branch_task',
       provide_context=True,
       python_callable=branch_test,
       dag=dag)

even_day_task = DummyOperator(task_id='even_day_task', dag=dag)
even_day_task2 = DummyOperator(task_id='even_day_task2', dag=dag)

odd_day_task = DummyOperator(task_id='odd_day_task', dag=dag)
odd_day_task2 = DummyOperator(task_id='odd_day_task2', dag=dag)

start_task >> branch_task 
branch_task >> even_day_task >> even_day_task2
branch_task >> odd_day_task >> odd_day_task2

from logging import exception
from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator,BranchPythonOperator
from symbol import raise_stmt
import random
from datetime import datetime ,timedelta
args={'owner':"abdo95",
'start_date':days_ago(1)

}
def run_this_func(**context):
    random_value=random.random()
    context['ti'].xcom_push(key='random_value',value=random_value)
    print("i am okay")

def print_hello(**context):
    recived_value=context['ti'].xcom_pull(key='random_value')
    print(f'hello I received the following{recived_value}')



def print_hi(**context):
    recived_value=context['ti'].xcom_pull(key='random_value')
    print(f'hiii I received the following{recived_value}')

def branch_func(**context):
    recived_value=context['ti'].xcom_pull(key='random_value')
    if recived_value < 0.5:
        return 'say_hi'
    return 'say_hello'
dag=DAG('mysample_d',default_args=args, description='Python DAG',schedule_interval=None)
with dag:
   run_this_task=PythonOperator(
    task_id='run_id', 
    python_callable=run_this_func,

    retries=10,
    retry_delay=timedelta(seconds=1),
    provide_context=True)
   
   branch_op=BranchPythonOperator(
    task_id='branch_id',
    python_callable=branch_func,
    provide_context=True
   )

   run_task2=PythonOperator(task_id='say_hi',
    python_callable=print_hi,
    provide_context=True)
 
   run_task3=PythonOperator(task_id='say_hello',
    python_callable=print_hello
    ,provide_context=True)
    
    
   run_this_task >> branch_op >> [run_task2,run_task3]
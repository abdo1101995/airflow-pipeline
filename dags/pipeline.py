from email.policy import default
from airflow.models import DAG
from datetime import datetime
from airflow.operators.bash_operator import BashOperator
default_arguments={
    'owner':'abdo',
    'email':'abomahmud7211@gmail.com',
    'start_date':datetime(2022,9,20)
}
etl_dag=DAG('etl_workflow',default_args=default_arguments)
# Define the BashOperator 
cleanup =BashOperator(
    task_id='cleanup_task',
    # Define the bash_command
    bash_command='echo clean',
    # Add the task to the dag
    dag=etl_dag
)
pull_sales =BashOperator(
    task_id='pullsales_task',
    bash_command='echo "pull"',
    dag=etl_dag
)

cleanup>>pull_sales
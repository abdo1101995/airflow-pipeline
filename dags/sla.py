# Import the timedelta object
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.bash_operator import BashOperator
# Create the dictionary entry
test_dag = DAG('test_workflow', start_date=datetime(2020,2,20), schedule_interval='@None')

# Create the task with the SLA
task1 = BashOperator(task_id='first_task',
                     sla=timedelta(hours=3),
                     bash_command='initialize_data.sh',
                     dag=test_dag)
                     # Define the email task
email_report =EmailOperator(
        task_id='email_report',
        to='airflow@datacamp.com',
        subject='Airflow Monthly Report',
        html_content="""Attached is your monthly workflow report - please refer to it for more detail""",
        files=['monthly_report.pdf'],
        dag=test_dag
)

# Set the email task to run after the report is generated
task1 >> email_report
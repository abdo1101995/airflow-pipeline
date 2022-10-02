from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.contrib.sensors.file_sensor import FileSensor

dag = DAG(
   dag_id = 'update_state',
   default_args={"start_date": "2019-10-01"}
)

precheck = FileSensor(
   task_id='check_for_datafile',
   filepath='D:\docker-airflow\Maiszuensler.csv',
   dag=dag)

part1 = BashOperator(
   task_id='generate_random_number',
   bash_command='echo $RANDOM',
   dag=dag
)

import sys
def python_version():
   return sys.version

part2 = PythonOperator(
   task_id='get_python_version',
   python_callable=python_version,
   dag=dag)
   
part3 = SimpleHttpOperator(
   task_id='query_server_for_external_ip',
   endpoint='https://api.ipify.org',
   method='GET',
   dag=dag)
   
precheck >> part3 >> part2
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='ingestao_cliente',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    tarefa_1 = BashOperator(
        task_id='imprimir_mensagem',
        bash_command='echo "Olá, Airflow!"'
    )
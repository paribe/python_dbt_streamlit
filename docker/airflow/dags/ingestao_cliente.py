from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 5),
    'retries': 1,
}

dag = DAG(
    'ingestao_cliente',
    default_args=default_args,
    description='DAG para orquestrar ingestão de clientes',
    schedule_interval='@daily',
)

# 1️⃣ Gerar arquivo CSV
generate_csv = BashOperator(
    task_id='generate_csv',
    bash_command='python /opt/airflow/ingestion/generate_csv.py',  # Caminho correto
    dag=dag,
)

# 2️⃣ Inserir no banco
ingest_db = BashOperator(
    task_id='ingest_db',
    bash_command='python /opt/airflow/ingestion/main.py',  # Caminho correto
    dag=dag,
)

# 3️⃣ Executar dbt run
run_dbt = BashOperator(
    task_id='run_dbt',
    bash_command='dbt run --profiles-dir /opt/airflow/dbt/',  # Caminho correto
    dag=dag,
)

# Definir a ordem das tarefas
generate_csv >> ingest_db >> run_dbt
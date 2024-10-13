from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello World from external_user DAG!")

with DAG(
    dag_id="hello_world_external_user_test_access",
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    access_control={
        'external_user': {'can_read', 'can_edit', 'can_dag_run'},  # Доступ для external_user
        'Admin': {'can_read', 'can_edit', 'can_dag_run'},  # Доступ для администратора
        'Viewer': {'can_read'},  # Просмотр для привилегированных пользователей
    },
    tags=['external_user'],  # Тег для фильтрации
) as dag:
    
    hello_world_task = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world
    )

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def hello_world():
    print("Hello from Apache Airflow running on GitHub Actions!")


with DAG(
    dag_id="hello_airflow_github_actions",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["github-actions", "beginner"],
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world,
    )

    hello_task
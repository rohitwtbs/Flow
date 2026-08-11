from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    dag_id='local_quickstart_dag',
    default_args=default_args,
    description='Sample Airflow DAG to test your local Docker Compose setup',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example', 'local'],
)
def local_quickstart_dag():

    @task()
    def start_task():
        print("🚀 Starting the local Airflow DAG pipeline!")
        return {"status": "started", "timestamp": str(datetime.now())}

    @task()
    def process_data(data: dict):
        print(f"⚡ Processing data received from previous task: {data}")
        processed = {
            "status": "success",
            "records_processed": 100,
            "processed_at": str(datetime.now())
        }
        return processed

    @task()
    def end_task(results: dict):
        print(f"🎉 Pipeline completed successfully! Final results: {results}")

    # Define task dependencies using TaskFlow API returns
    initial_data = start_task()
    results = process_data(initial_data)
    end_task(results)

# Instantiate the DAG
local_quickstart_dag()

from datetime import datetime, timedelta

from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sdk import DAG

IMAGE = "ghcr.io/peauc/kraken-bootstrap-lab-test:e464a52c1b225f6e9f62e2ae689d8db246babc55"

with DAG(
    dag_id="kraken_bootstrap",
    schedule="0 6 * * *",
    start_date=datetime(2026, 11, 1),
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=5)},
    tags=["kraken"],
):
    DockerOperator(
        task_id="run_job",
        image=IMAGE,
        execution_timeout=timedelta(minutes=30),
        mount_tmp_dir=False,
        auto_remove="success",
    )

from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner':'harryli',
    'retries':5,                        # 執行失敗時要重試幾次
    'retry_delay':timedelta(minutes=2)  # 執行失敗時，過多久才重試
}


with DAG(
    dag_id = 'our_first_dag_v5',
    default_args = default_args,
    description = 'this is our first that we write',
    start_date = datetime(2022, 6, 13, 2),
    schedule_interval = '@daily',
)as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = 'echo hellow world, this is the first task!'
    )
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = 'echo hey, I am task2 and will be running after task1 ~'
    )

    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = 'echo hey, I am task3 and will be running after task1 at the same time task2.'
    )

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]
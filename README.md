# Airflow-practice

Apache Airflow 工作流程管理平臺
 - WebServer : 圖形化介面
 - Scheduler : 負責排程、監控 DAG
 - Worker : 排成的工作交給worker執行


DAG
- 每個工作流程被定義為有向無環圖，每個dag包含各種工作(task)集合。

Operators(每個工作的工作內容)
- BashOperator : 執行 bash 指令
- PythonOperator : 執行 Python function
- EmailOperator : 發送郵件
- HttpOperator : 發送http請求
- MysqlOperator : 連接資料庫

Task
- 工作內容


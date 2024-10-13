# airflow-cluster
 

# Example

## Dataset and auto train after update S3 dataset

https://airflow.apache.org/docs/apache-airflow/2.9.3/authoring-and-scheduling/datasets.html

Пример показывает, как использовать датасет в качестве триггера для запуска DAG после обновления данных:

```python
from airflow.datasets import Dataset

example_dataset = Dataset("s3://dataset/example.csv")

with DAG(dag_id="producer", ...):
    BashOperator(task_id="producer", outlets=[example_dataset], ...)

with DAG(dag_id="consumer", schedule=[example_dataset], ...):
    ...
```

Этот код показывает, как DAG потребителя запускается после успешного завершения задачи в DAG производителя, которая обновляет датасет.

 
# To-Do

- [ ] add CPU k8s label for 003
- [ ] add CPU k8s label for 004

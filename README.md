# query-lakehouse

This is a Lambda function written in Python that is deployed as a container image

It implements a basic query function that accepts a SQL query and returns the response in JSON format

Behind the scenes, it connects to a serverless SQL Warehouse running at `enb-colab.cloud.databricks.com`

USAGE (Python)
```python
import lakehouse_client
lakehouse_client.query_lakehouse("SELECT * FROM hive_metastore.default.diamonds LIMIT 3;")
```


def query_databricks(query):
    from databricks import sql
    from chalicelib import mysecrets
    import urllib.parse
    import os

    connection = sql.connect(
                            mysecrets.server_hostname,
                            mysecrets.http_path,
                            mysecrets.access_token)

    cursor = connection.cursor()

    cursor.execute(urllib.parse.unquote_plus(query))
    columns = [column[0] for column in cursor.description]  # https://stackoverflow.com/questions/16519385/output-pyodbc-cursor-results-as-python-dictionary
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    cursor.close()
    connection.close()
    return results


def lambda_handler(event, context):
    return query_databricks(event['query'])  # "SELECT 1;"

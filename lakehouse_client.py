def query_lakehouse(query="SELECT 1;"):
    import boto3, json
    lam = boto3.client('lambda')
    payload = bytes(json.dumps({'query': query}), 'utf8')
    response = lam.invoke(FunctionName='query-lakehouse', InvocationType='RequestResponse', Payload=payload)
    return json.loads(response['Payload'].read())
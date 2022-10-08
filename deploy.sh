export AWS_PROFILE=aws-field-eng_databricks-power-user
export AWS_DEFAULT_REGION=us-east-1

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 997819012307.dkr.ecr.us-east-1.amazonaws.com

docker tag query-lakehouse:latest 997819012307.dkr.ecr.us-east-1.amazonaws.com/query-lakehouse:latest

docker push 997819012307.dkr.ecr.us-east-1.amazonaws.com/query-lakehouse:latest

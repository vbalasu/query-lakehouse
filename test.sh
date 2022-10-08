curl -XPOST "http://localhost:9001/2015-03-31/functions/function/invocations" \
 -d '{"query": "SELECT 1;"}' | python -m json.tool
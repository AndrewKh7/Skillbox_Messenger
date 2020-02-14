import requests as rq
import json

res = rq.get("http://localhost:5000/status")
print(res.status_code)
print(res.text)
data = json.loads(res.text)
print(data)
for k in data:
    print(k, data[k])
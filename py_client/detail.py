import requests

endpoint = 'http://localhost:8000/api/products/1/'
res = requests.get(endpoint)
print(res.json())
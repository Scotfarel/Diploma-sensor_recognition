import requests

url = "http://127.0.0.1:8000/db/get/"
data = {'requyavik': 2020,
        }

r = requests.get(url, data)
print(r.content)

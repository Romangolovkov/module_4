import requests


res = requests.get("http://numbersapi.com/7/22/date")
print(res.json)
print(res.text)
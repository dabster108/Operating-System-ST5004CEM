import requests 
URL = "http://127.0.0.1:5002/api/uppercase"

for t in ["hello", "world"]:
    payload = {"text": t}
    response = requests.post(URL, json=payload)
    print('SENT', t)
    print('Response:', response.json())

    
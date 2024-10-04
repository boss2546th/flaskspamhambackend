import requests
url = "http://127.0.0.1:5000/predict"

try:
    msg = {'message':str(input('message : '))}
    r = requests.post(url, json = msg)
    print(r.text)
except:
    print('error')
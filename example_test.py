import requests

# Simple test script - execute when the app is running
url = "http://127.0.0.1:5000"
one_address = "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3"
res = requests.post(url, params={"address": one_address}).json()
print(res)

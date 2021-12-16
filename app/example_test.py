import requests

# Simple test script - execute when the app is running
url = "http://one-to-eth-ddo5p.ondigitalocean.app"
one_address = "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3"
res = requests.post(url, params={"address": one_address}).text
print(res)

import requests

# Simple test script - execute when the app is running
url = "http://134.209.89.7:8000"
one_address = "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3"
params = {"address": one_address}
res = requests.post(url, params=params).json()
print(res)

### Returns ...
{
    "status": "success", 
    "message": "ONE Address one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3 converted to 0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32", 
    "one_address": "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3", 
    "eth_address": "0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32"
    }
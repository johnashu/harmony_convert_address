import requests

# Simple test script - execute when the app is running
url = "http://<address_of_docker_container>:8000"
one_address = "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3"
res = requests.post(url, params={"address": one_address}).text
print(res)

### Returns ...
{"status": "success", "message": "ONE Address one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3 converted to 0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32", "one_address": "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3", "eth_address": "0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32"}
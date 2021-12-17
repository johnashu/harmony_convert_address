import requests

# Simple test script - execute when the app is running
url = "http://127.0.0.1:5000"

one_addresses = [
    "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3",
    "one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf",
    "one1ltlmxwujfsens80wxh2y2qfaxgqzf9tjex3fc2",
    "somewrongaddress",
]
params = {"address": one_addresses}
res = requests.post(url, params=params).json()
print(res)

### Returns ...
[
    {
        "status": "success",
        "message": "ONE Address one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3 Successfully converted to 0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32",
        "one_address": "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3",
        "eth_address": "0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32",
    },
    {
        "status": "success",
        "message": "ONE Address one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf Successfully converted to 0x08c4596B157EafAE5EC4E0fE629005Bab2a10C3D",
        "one_address": "one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf",
        "eth_address": "0x08c4596B157EafAE5EC4E0fE629005Bab2a10C3D",
    },
    {
        "status": "success",
        "message": "ONE Address one1ltlmxwujfsens80wxh2y2qfaxgqzf9tjex3fc2 Successfully converted to 0xfAFfb33B924C33381dee35D445013D3200249572",
        "one_address": "one1ltlmxwujfsens80wxh2y2qfaxgqzf9tjex3fc2",
        "eth_address": "0xfAFfb33B924C33381dee35D445013D3200249572",
    },
    {
        "status": "error",
        "message": "ONE Address somewrongaddress was NOT converted, ERROR: when sending a str, it must be a hex string. Got: 'somewrongaddress'",
        "one_address": "somewrongaddress",
        "eth_address": "error converting",
    },
]

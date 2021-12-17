# ONE Address -> ETH Address

Base Service to convert One Addresses to ETH format and serve results via API POST request.
# Run with Docker

On an OS with Docker installed.

`docker-compose build`

`docker-compose up`

# Test program Locally

Start the service

`python3 main.py`

Set the url in `tests/test_api.py` 

i.e. `url = "http://127.0.0.1:5000"`

Run the tests

`pytest`

``` bash

>>> pytest

============================================ test session starts ============================================= 
platform win32 -- Python 3.8.5, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\J3876544\Documents\GIT\one_to_eth
plugins: web3-5.25.0
collected 3 items                                                                                              

tests\test_api.py ...                                                                                   [100%] 

============================================= 3 passed in 0.10s ============================================== 

```

Example responses:

> Happy Flow

```json
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

```

> Errors

``` json

 [
        {
            "error": "Incorrect request, please supply parameter addresses with an array of addresses to convert"
        }
    ]

[
    {
        "error": "Empty Request"
        }
]

[
    {
        "status": "error",
        "message": "ONE Address somewrongaddress was NOT converted, ERROR: when sending a str, it must be a hex string. Got: 'somewrongaddress'",
        "one_address": "somewrongaddress",
        "eth_address": "error converting",
    }
]

```


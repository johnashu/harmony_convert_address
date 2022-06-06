# ONE Address <> ETH Address

Asynchronous Base Service to convert ONE Addresses to ETH format and from ETH Addresses to ONE Format (Bech32)

Serves results via API POST request.
# Run with Docker

On an OS with Docker installed.

`docker-compose build`

`docker-compose up`

# Run locally

`python3 main.py`

# Build Request

Example with Python

```python
import requests

# define URL
url = "http://127.0.0.1:5000"

# create list with addresses to convert - ONE / ETH
one_addresses = [
    "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3",
    "one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf",
    "one1ltlmxwujfsens80wxh2y2qfaxgqzf9tjex3fc2",
    "somewrongaddress",
]

# build params using "addresses" key
params = {
    "addresses": one_addresses, 
    "from_address": "one"
    }

# send request
response = requests.post(url, params=params)
print(f"{response.json()}\n")

```

# Curl Example

Curl requests can be displayed by running `python3 test_api.py`

To add specific headers update `headers = None` in `test_api.py` to a dictionary of headers.

Look for the following in the logs output or check the `api_tests.log`

```
[INFO]: cURL Request:
curl -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate" -H "Connection: keep-alive" -H "Content-Length: 0" -H "User-Agent: python-requests/2.26.0" "http://127.0.0.1:5000/?addresses=one137ur0lcdd067he326kkp7g477d0epfkw9lplh6&addresses=one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf
```

To convert CURL requests to example code for languages other than python - use https://curlconverter.com/

```curl
curl -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate" -H "Connection: keep-alive" -H "Content-Length: 0" -H "User-Agent: python-requests/2.24.0" "http://127.0.0.1:5000/?addresses=one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3&addresses=one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf&addresses=one1ltlmxwujfsens80wxh2y2qfaxgqzf9tjex3fc2&addresses=somewrongaddress"
```

# Test Program

Start the service locally or remotely

`python3 main.py`

Set the url in `tests/test_api.py` 

i.e. `url = "http://127.0.0.1:5000"`

Run the tests

`pytest`

``` bash

>>> pytest

============================================ test session starts ============================================= 
platform win32 -- Python 3.8.5, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\JohnAshurst\Documents\GIT\one_to_eth
plugins: web3-5.25.0
collected 3 items                                                                                              

tests\test_api.py ...                                                                                   [100%] 

============================================= 3 passed in 0.10s ============================================== 

```

# Example responses:

> Happy Flow

```json
[
    {
        "status": "success",
        "message": "ETH Address [ 0x8fb837ff0d6bf5ebE62aD5aC1f22BEF35F90a6ce ]  Successfully converted to ONE Address [ one137ur0lcdd067he326kkp7g477d0epfkw9lplh6 ]",
        "eth_address": "0x8fb837ff0d6bf5ebE62aD5aC1f22BEF35F90a6ce",
        "one_address": "one137ur0lcdd067he326kkp7g477d0epfkw9lplh6"
    },
    {
        "status": "success",
        "message": "ETH Address [ 0x08c4596B157EafAE5EC4E0fE629005Bab2a10C3D ]  Successfully converted to ONE Address [ one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf ]",
        "eth_address": "0x08c4596B157EafAE5EC4E0fE629005Bab2a10C3D",
        "one_address": "one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf"
    },
    {
        "status": "error",
        "message": "ETH Address [ somewrongaddress ]  was NOT converted, ERROR: ONE", 
        "eth_address": "somewrongaddress", 
        "one_address": "error converting"}]

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
        "message": "ONE Address somewrongaddress was NOT converted, ERROR: when sending a str, it must be a hex string. Got: 'somewrongaddress' ",
        "one_address": "somewrongaddress",
        "eth_address": "error converting",
    }
]

```

Donations appreciated: one1xlu2vumced5sm5qtmxx27sekec8hcdc3maffaz



# ONE Address -> ETH Address

Service to convert One Addresses to ETH format

# Run with Docker

On an OS with Docker installed.

`docker-compose build`

`docker-compose up`

# Test program Locally

Start the service

`python3 main.py`

Set the url in `example_test.py` 

`url = "http://127.0.0.1:5000"`

Run the test

`python3 example_test.py`

Example response:

```json
{
    "status": "success", 
    "message": "ONE Address one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3 converted to 0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32", 
    "one_address": "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3", 
    "eth_address": "0xc3a097Fc607Dc41b83bE280E170e7A0cc42bBb32"
    }

```

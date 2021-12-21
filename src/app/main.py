import uvicorn
import urllib.parse, json
import logging

from core.convert import convert_one_to_hex
from includes.messages import *

print(http_response_body, http_response_start)


async def process_addresses(addresses: list) -> list:
    body = []
    for one_address in addresses:
        status, eth_address = await convert_one_to_hex(one_address)

        msg = f"ONE Address {one_address} {res_status[status].format(eth_address)}"
        body.append(
            {
                "status": status,
                "message": msg,
                "one_address": one_address,
                "eth_address": eth_address if status != "error" else "error converting",
            }
        )

    return body


async def send_response(send, body: list, status: int = 200):
    await send(dict(http_response_start, **{"status": status}))
    body = json.dumps(body).encode("utf-8")
    await send(dict(http_response_body, **{"body": body}))


async def app(scope, receive, send):
    assert scope["type"] == "http"
    q = scope["query_string"]
    # log.info(scope)
    if not q:
        body = [{"error": empty_msg}]
        await send_response(send, body, status=400)
    else:
        params = dict(urllib.parse.parse_qs(q.decode()))
        addresses = params.get("addresses")
        if not addresses:
            body = [{"error": bad_request_msg}]
            await send_response(send, body, status=400)
        else:
            body = await process_addresses(addresses)
            await send_response(send, body)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)

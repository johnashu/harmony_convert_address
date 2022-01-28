import uvicorn
import urllib.parse, json
import logging

from core.convert import convert_one_to_eth, convert_eth_to_one
from includes.messages import *


async def process_addresses(addresses: list, convert_from_address: str) -> list:
    func = convert_one_to_eth
    convert_to_address = "eth"
    if convert_from_address == "eth":
        func = convert_eth_to_one
        convert_to_address = "one"
    body = []
    for address in addresses:
        status, converted_address = await func(address)

        msg = f"{convert_from_address.upper()} Address [ {address} ]  {res_status[status].format(convert_to_address.upper(), converted_address)}"
        body.append(
            {
                "status": status,
                "message": msg,
                f"{convert_from_address}_address": address,
                f"{convert_to_address}_address": converted_address
                if status != "error"
                else "error converting",
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
    logging.info(q)
    if not q:
        body = [{"error": empty_msg}]
        await send_response(send, body, status=400)
    else:
        params = dict(urllib.parse.parse_qs(q.decode()))
        addresses = params.get("addresses")
        from_address = params.get("from_address")
        if not addresses:
            body = [{"error": bad_request_msg}]
            await send_response(send, body, status=400)
        else:
            body = await process_addresses(addresses, from_address[0])
            await send_response(send, body)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)

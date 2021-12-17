import uvicorn
import urllib.parse, json
import logging as log

from core.convert import convert_one_to_hex


async def process_addresses(addresses: list) -> list:
    body = []
    for one_address in addresses:
        res, eth_address = await convert_one_to_hex(one_address)
        status = "success"
        no_yes = f"Successfully converted to {eth_address}"
        if not res:
            status = "error"
            no_yes = f"was NOT converted, ERROR: {eth_address}"

        msg = f"ONE Address {one_address} {no_yes}"

        body.append(
            {
                "status": status,
                "message": msg,
                "one_address": one_address,
                "eth_address": eth_address if res else "error converting",
            }
        )

    return json.dumps(body).encode("utf-8")


async def send_400(send, msg):
    await send(
        {
            "type": "http.response.start",
            "status": 400,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )
    body = [{"error": msg}]
    body = json.dumps(body).encode("utf-8")
    await send({"type": "http.response.body", "body": body})


async def app(scope, receive, send):
    assert scope["type"] == "http"
    q = scope["query_string"]
    # log.info(scope)
    if not q:
        empty_msg = "Empty Request"
        await send_400(send, empty_msg)
    else:
        params = dict(urllib.parse.parse_qs(q.decode()))
        addresses = params.get("addresses")
        if not addresses:
            bad_request_msg = "Incorrect request, please supply parameter `addresses`  with an array of addresses to convert"
            await send_400(send, bad_request_msg)
        else:
            body = await process_addresses(addresses)
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                }
            )
            await send({"type": "http.response.body", "body": body})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)

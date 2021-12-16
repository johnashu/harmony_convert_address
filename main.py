import uvicorn
import urllib.parse, json

from core import convert


async def app(scope, receive, send):
    assert scope["type"] == "http"

    # print(scope)

    params = dict(urllib.parse.parse_qs(scope["query_string"].decode()))
    one_address = params["address"][0]
    eth_address = await convert.convert_one_to_hex(one_address)

    msg = f"ONE Address {one_address} converted to {eth_address}"

    body = json.dumps(
        {
            "status": "success",
            "message": msg,
            "one_address": one_address,
            "eth_address": eth_address,
        }
    ).encode("utf-8")

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
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")

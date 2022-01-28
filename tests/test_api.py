import requests
import curlify
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s]: %(message)s")
# Simple test script - execute when the app is running
url = "http://127.0.0.1:5000"

# Addresses should be correct to check that it converted correctly.
one_addresses = [
    "one137ur0lcdd067he326kkp7g477d0epfkw9lplh6",
    "one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf",
    "somewrongaddress",
]

eth_addresses = [
    "0x8fb837ff0d6bf5ebE62aD5aC1f22BEF35F90a6ce",
    "0x08c4596B157EafAE5EC4E0fE629005Bab2a10C3D",
    "somewrongaddress",
]

happy_flow = {"addresses": one_addresses, "from_address": "one"}
happy_flow_eth = {"addresses": eth_addresses, "from_address": "eth"}
wrong_address = {"addresses": ["somewrongaddress"], "from_address": "one"}
wrong_key = {"wrong_key": "", "from_address": "one"}
empty_request = {"addresses": [], "from_address": "one"}

headers = None


def make_request(params: dict, url: str = url, headers: list = None) -> list:
    res = requests.post(url, params=params, headers=headers)
    # logging.info Response
    logging.info(f"{res.json()}\n")
    # logging.info cURL request..
    logging.info(f"cURL Request:\n{curlify.to_curl(res.request)}\n")
    return res.json()


def base(params: tuple, expected: str, status: str = None, **kw) -> None:
    for p in params:
        r = make_request(p, **kw)
        exp_res = r[0].get(expected)
        assert exp_res, f"Expected: {exp_res} | Got: {status}"
        if status:
            assert exp_res == status, f"Expected: {exp_res} | Got: {status}"
        for x in r:
            if x.get("status") == "success":
                eth = x["eth_address"]
                idx = eth_addresses.index(eth)
                logging.info(eth)
                assert (
                    one_addresses[idx] == x["one_address"]
                ), f"Expected: {one_addresses[idx]} | Got: {x['one_address']}"


def test_happy_flow(**kw) -> None:
    base((happy_flow,), "status", status="success", **kw)
    base((happy_flow_eth,), "status", status="success", **kw)


def test_wrong_address(**kw) -> None:
    base((wrong_address,), "status", **kw)
    base((wrong_address.update({"from_address": "eth"}),), "error", **kw)


def test_error_responses(**kw) -> None:
    base((wrong_key, empty_request), "error", **kw)
    base((wrong_key.update({"from_address": "eth"}), empty_request), "error", **kw)


if __name__ == "__main__":
    kw = dict(url=url, headers=headers)

    # test request
    params = {"addresses": "SomeAddress", "from_address": "one"}
    make_request(params, **kw)

    # manual check tests. - uncomment to run.
    test_happy_flow(**kw)
    test_error_responses(**kw)
    test_wrong_address(**kw)

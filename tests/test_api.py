import requests

import curlify

# Simple test script - execute when the app is running
url = "http://127.0.0.1:5000"

one_addresses = [
    "one1cwsf0lrq0hzphqa79q8pwrn6pnzzhwej4tqen3",
    "one1prz9j6c406h6uhkyurlx9yq9h2e2zrpasr2saf",
    "one1ltlmxwujfsens80wxh2y2qfaxgqzf9tjex3fc2",
    "somewrongaddress",
]

happy_flow = {"addresses": one_addresses}
wrong_address = {"addresses": ["somewrongaddress"]}
wrong_key = {"wrong_key": ""}
empty_request = {"addresses": []}

headers = None


def make_request(params: dict, url: str = url, headers: list = None) -> list:
    res = requests.post(url, params=params, headers=headers)
    print(f"{res.json()}\n")
    print(f"{curlify.to_curl(res.request)}\n")
    return res.json()


def base(params: list, expected: str, status: str = None, **kw) -> None:
    for p in params:
        r = make_request(p, **kw)
        assert r[0].get(expected)
        if status:
            assert r[0].get(expected) == status


def test_happy_flow(**kw) -> None:
    base((happy_flow,), "status", **kw)


def test_wrong_address(**kw) -> None:
    base((wrong_address,), "status", status="error", **kw)


def test_error_responses(**kw) -> None:
    base((wrong_key, empty_request), "error", **kw)


if __name__ == "__main__":

    kw = dict(url=url, headers=headers)

    # test request
    params = {"addresses": "SomeAddress"}
    make_request(params, **kw)

    # manual check tests. - uncomment to run.

    # test_happy_flow(**kw)
    # test_error_responses(**kw)
    # test_wrong_address(**kw)

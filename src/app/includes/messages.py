http_response_start = {
    "type": "http.response.start",
    "status": 200,
    "headers": [
        [b"content-type", b"text/plain"],
    ],
}
http_response_body = {"type": "http.response.body", "body": [{b"hello": b"world"}]}

res_status = {
    "success": "Successfully converted to {}",
    "error": "was NOT converted, ERROR: {}",
}

empty_msg = "Empty Request"
bad_request_msg = "Incorrect request, please supply parameter `addresses`  with an array of addresses to convert"

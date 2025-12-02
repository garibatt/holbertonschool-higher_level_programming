from urllib import request

url = "https://intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()

    print("Body response:")
    print("    - type:", type(body))
    print("    - content:", body)
    print("    - utf8 content:", body.decode("utf-8"))

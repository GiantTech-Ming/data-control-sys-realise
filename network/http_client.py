# network/http_client.py
# HTTP客户端模块

class HTTPClient:
    def get(self, url):
        print(f"Sending GET request to {url}")

    def post(self, url, data):
        print(f"Sending POST request to {url} with data {data}")
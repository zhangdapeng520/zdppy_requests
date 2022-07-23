import zdppy_requests

proxies = {
    "http": "http://user:password@127.0.0.1:9743/",
}
response = zdppy_requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)
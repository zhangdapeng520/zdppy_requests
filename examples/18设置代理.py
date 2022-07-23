import zdppy_requests

proxies = {
    "http": "http://127.0.0.1:9743",
    "https": "https://127.0.0.1:9743",
}

# 往请求中设置代理(proxies
response = zdppy_requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)

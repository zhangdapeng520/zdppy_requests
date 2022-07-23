import zdppy_requests

proxies = {
    'http': 'socks5://127.0.0.1:9742',
    'https': 'socks5://127.0.0.1:9742'
}
response = zdppy_requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)

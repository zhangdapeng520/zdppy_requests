import zdppy_requests

# 设置本地证书
response = zdppy_requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)
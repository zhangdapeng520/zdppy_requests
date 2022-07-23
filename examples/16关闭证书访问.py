import zdppy_requests

# 关闭验证，但是仍然会报出证书警告
response = zdppy_requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

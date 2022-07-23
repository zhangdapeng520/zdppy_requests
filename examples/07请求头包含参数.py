import zdppy_requests

# GET请求参数
param = {'name': 'ide', 'city': 'New York'}

# 传递参数params
response = zdppy_requests.get('http://httpbin.org/get', params=param)
print(response.text)

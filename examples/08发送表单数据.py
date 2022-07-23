import zdppy_requests

# POST请求参数
param = {'name': 'ide', 'city': 'New York'}

# 传递参数params
response = zdppy_requests.post('http://httpbin.org/post', data=param)
print(response.text)

import json
import zdppy_requests

# POST请求参数
param = {'name': 'ide', 'city': 'New York'}

# 传递参数params，并格式化为json数据
response = zdppy_requests.post('http://httpbin.org/post', data=json.dumps(param))
print(response.text)

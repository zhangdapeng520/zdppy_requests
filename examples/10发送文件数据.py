import zdppy_requests

# POST请求参数
file = {'file': open('01发送请求.py', 'rb')}

# 传递参数files
response = zdppy_requests.post('http://httpbin.org/post', files=file)
print(response.text)

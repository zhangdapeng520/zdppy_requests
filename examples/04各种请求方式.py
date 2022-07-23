import zdppy_requests

# 发起POST请求
r = zdppy_requests.post('http://httpbin.org/post')
print(r)

# 发起PUT请求
r = zdppy_requests.put('http://httpbin.org/put')
print(r)

# 发起DELETE请求
r = zdppy_requests.delete('http://httpbin.org/delete')
print(r)

# 发送HEAD请求
r = zdppy_requests.head('http://httpbin.org/get')
print(r)

# 发送OPTION请求
r = zdppy_requests.options('http://httpbin.org/get')
print(r)

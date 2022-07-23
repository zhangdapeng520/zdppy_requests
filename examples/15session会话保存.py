import zdppy_requests

# 从requests中获取session
session = zdppy_requests.session()

# 使用seesion去请求保证了请求是同一个session
session.get('http://httpbin.org/cookies/set/number/12456')
response = session.get('http://httpbin.org/cookies')
print(response.text)

# 引入Requests库
import zdppy_requests

# 发起GET请求
r = zdppy_requests.get('https://www.baidu.com/')

# 查看响应类型  requests.models.Response
print(type(r))

# 输出状态码  200
print(r.status_code)

# 输出响应内容类型  str
print(type(r.text))

# 输出响应内容
print(r.text)

# 输出cookies
print(r.cookies)

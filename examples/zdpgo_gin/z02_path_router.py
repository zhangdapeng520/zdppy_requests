from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

response = r.get("/user/zhangdapeng")
print(response)
print(response.status_code)
print(dir(response))
print(response.content)
print(response.content.decode())  # 手动解码

print(r.get("/user/zhangdapeng/create_token").text)  # 自动解码

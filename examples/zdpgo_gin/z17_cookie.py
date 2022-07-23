from zdppy_requests import Requests, Cookie

r = Requests(port=8888, debug=True)

# 新增token
response = r.post("/cookie")
print(response.json())
print(response.cookies)
token = response.cookies["token"]
print(token)

# 携带cookie
cookie_jar = Cookie()
cookie_jar.set("token", token, domain="*")
print(r.get("/cookie", cookies=cookie_jar).json())

# 删除cookie
response = r.delete("/cookie")
print(response.json())
print(response.cookies)

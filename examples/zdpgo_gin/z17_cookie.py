from zdppy_requests import Requests, Cookie

r = Requests(port=8888, debug=True)

# 新增token
response = r.post("/cookie")
r.log.info(response.json())
r.log.info(response.cookies)
token = response.cookies["token"]
r.log.info(token)

# 携带cookie
cookie_jar = Cookie()
cookie_jar.set("token", token, domain="*")
r.log.info(r.get("/cookie", cookies=cookie_jar).json())

# 删除cookie
response = r.delete("/cookie")
r.log.info(response.json())
r.log.info(response.cookies)

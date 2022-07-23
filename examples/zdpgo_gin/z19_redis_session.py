from zdppy_requests import Requests, Cookie

r = Requests(port=8080, debug=True)

# 获取session
print(r.get("/test").json())
print(r.get("/test").json())
print(r.get("/test").json())


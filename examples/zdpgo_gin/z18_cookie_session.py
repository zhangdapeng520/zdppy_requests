from zdppy_requests import Requests, Cookie

r = Requests(port=8080, debug=True)

# 获取session
r.log.info(r.get("/test").json())


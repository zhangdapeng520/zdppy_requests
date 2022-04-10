from zdppy_requests import Requests

r = Requests(port=8080, debug=True, username="zhangdapeng", password="zhangdapeng")

# 获取session
response = r.get("/admin/secrets")
r.log.debug(response.status_code)

if response.status_code == 200:
    r.log.debug(response.json())

from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

# 带auth请求
basic_auth = {
    "username": "zhangdapeng",
    "password": "zhangdapeng"
}
response = r.get("/admin/secrets", basic_auth=basic_auth)
r.log.debug(response.status_code)

if response.status_code == 200:
    r.log.debug(response.json())

# 不带auth请求
response = r.get("/health")
r.log.debug(response.status_code)

if response.status_code == 200:
    r.log.debug(response.json())

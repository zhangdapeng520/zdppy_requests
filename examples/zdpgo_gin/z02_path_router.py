from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

response = r.get("/user/zhangdapeng")
r.log.info(response)
r.log.info(response.status_code)
r.log.info(dir(response))
r.log.info(response.content)
r.log.info(response.content.decode())  # 手动解码

r.log.info(r.get("/user/zhangdapeng/create_token").text)  # 自动解码

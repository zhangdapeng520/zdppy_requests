from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

r.log.info(r.post("/v1/login").json())
r.log.info(r.post("/v1/logout").json())
r.log.info(r.post("/v2/login").json())
r.log.info(r.post("/v2/logout").json())

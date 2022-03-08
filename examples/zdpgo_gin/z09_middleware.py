from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

r.log.info(r.post("/login").json())
r.log.info(r.post("/logout").json())
r.log.info(r.get("/test").json())
r.log.info(r.post("/test1/abc").json())

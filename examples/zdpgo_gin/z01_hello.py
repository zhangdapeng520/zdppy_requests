from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

r.log.info(r.get("/").json())
r.log.info(r.post("/").json())
r.log.info(r.put("/").json())
r.log.info(r.delete("/").json())
r.log.info(r.patch("/").json())

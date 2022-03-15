from zdppy_requests import Requests

r = Requests(port=8888, debug=True)

json_data = {
    "name": "张大鹏",
    "age": 22,
}
r.log.info(r.get("/").json())
r.log.info(r.post("/a", json=json_data).json())
r.log.info(r.put("/a/b", json=json_data).json())
r.log.info(r.delete("/a/b/c", json=json_data).json())
r.log.info(r.patch("/a/b/c", json=json_data).json())

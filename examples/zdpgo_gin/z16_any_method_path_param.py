from zdppy_requests import Requests

r = Requests(port=8888, debug=True)

json_data = {
    "name": "张大鹏",
    "age": 22,
}
print(r.get("/").json())
print(r.post("/a", json=json_data).json())
print(r.put("/a/b", json=json_data).json())
print(r.delete("/a/b/c", json=json_data).json())
print(r.patch("/a/b/c", json=json_data).json())

from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

json_data = {
    "name": "张大鹏",
    "age": 22,
}
print(r.post("/", json=json_data).json())
print(r.put("/", json=json_data).json())
from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

print(r.get("/").json())
print(r.post("/").json())
print(r.put("/").json())
print(r.delete("/").json())
print(r.patch("/").json())

from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

print(r.post("/v1/login").json())
print(r.post("/v1/logout").json())
print(r.post("/v2/login").json())
print(r.post("/v2/logout").json())

from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

print(r.post("/login").json())
print(r.post("/logout").json())
print(r.get("/test").json())
print(r.post("/test1/abc").json())

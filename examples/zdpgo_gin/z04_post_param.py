from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

form = {
    "username": "张大鹏",
    "age": 33
}
print(r.post("/test", form=form).json())  # 自动解码

from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

query = {
    "page": 2,
    "size": 33,
}
form = {
    "username": "张大鹏",
    "age": 33
}
r.log.info(r.post("/test", query=query, form=form).json())  # 自动解码

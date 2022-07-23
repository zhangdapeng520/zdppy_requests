from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

query = {
    "first_name": "大鹏",
    "last_name": "张"
}
print(r.get("/welcome", query=query).text)  # 自动解码

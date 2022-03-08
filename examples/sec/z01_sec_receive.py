from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

headers = {
    "Sec": "1-sql",  # 格式：类型id-类型
}
json_data = {
    "payload": "测试payload",
}

# 成功
r.log.info(r.post("/api/v1/sec", json=json_data, headers=headers).json())

# 成功：任意路径
r.log.info(r.post("/a/b/c/d/e/f/g", json=json_data, headers=headers).json())
r.log.info(r.post("/", json=json_data, headers=headers).json())
r.log.info(r.post("", json=json_data, headers=headers).json())

# 失败：sec为空
r.log.info(r.post("/api/v1/sec", json=json_data).json())
r.log.info(r.post("/api/v1/sec").json())

# 失败：payload为空
r.log.info(r.post("/api/v1/sec", headers=headers).json())

from zdppy_requests import Requests
import time

r = Requests(port=8080, debug=True)

headers = {
    "Sec": "1-sql",  # 格式：类型id-类型
}
json_data = {
    "payload": "测试payload",
}


def test_request():
    """
    测试请求
    """
    # 成功：任意路径
    print(r.post("/a/b/c/d/e/f/g", json=json_data, headers=headers).json())
    print(r.post("/", json=json_data, headers=headers).json())
    print(r.post("", json=json_data, headers=headers).json())

    # 成功：方法
    print(r.get("/a/b/c/d/e/f/g", headers=headers).json())
    print(r.put("/a/b/c/d/e/f/g", json=json_data, headers=headers).json())
    print(r.delete("/a/b/c/d/e/f/g", json=json_data, headers=headers).json())
    print(r.patch("/a/b/c/d/e/f/g", json=json_data, headers=headers).json())

    # 失败：sec为空
    print(r.post("/api/v1/sec", json=json_data).json())
    print(r.post("/api/v1/sec").json())

    # 失败：payload为空
    print(r.post("/api/v1/sec", headers=headers).json())


def test_thread(num):
    """
    测试请求
    """
    start_time = time.time()
    for i in range(num):
        # 成功
        print(r.post("/api/v1/sec", json=json_data, headers=headers).json())
    print(time.time() - start_time)


if __name__ == '__main__':
    # test_request()
    test_thread(10000)  # 测试单线程请求n次

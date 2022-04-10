from zdppy_requests import Requests
import time

r = Requests(port=8080, debug=True)

headers = {
    "Sec": "1-sql",  # 格式：类型id-类型
}
json_data = {
    "payload": "测试payload",
}

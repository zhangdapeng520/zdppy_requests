import zdppy_requests
from zdppy_requests.exceptions import ReadTimeout

try:
    # 设置必须在500ms内收到响应，不然或抛出ReadTimeout异常
    response = zdppy_requests.get("http://httpbin.org/get", timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')

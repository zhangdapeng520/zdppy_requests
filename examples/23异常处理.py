import zdppy_requests
from zdppy_requests.exceptions import ReadTimeout, ConnectionError, RequestException

try:
    response = zdppy_requests.get("http://httpbin.org/get", timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    # 超时异常
    print('Timeout')
except ConnectionError:
    # 连接异常
    print('Connection error')
except RequestException:
    # 请求异常
    print('Error')

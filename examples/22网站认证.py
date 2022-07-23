import zdppy_requests
from zdppy_requests.auth import HTTPBasicAuth

response = zdppy_requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
print(response.status_code)

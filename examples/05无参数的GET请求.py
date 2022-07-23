import zdppy_requests

response = zdppy_requests.get('http://httpbin.org/get')
print(response.text)

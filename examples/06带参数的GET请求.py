import zdppy_requests

response = zdppy_requests.get('http://httpbin.org/get?name=jyx&age=18')
print(response.text)

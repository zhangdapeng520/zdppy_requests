import zdppy_requests

url = 'http://httpbin.org/cookies'
cookies = {'mycookies': 'working'}

response = zdppy_requests.get(url, cookies=cookies)
print(response.text)

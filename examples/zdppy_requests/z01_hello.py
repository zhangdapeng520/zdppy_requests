from zdppy_requests import requests

response = requests.get("https://www.baidu.com/")
print(response.status_code)
print(response.text)

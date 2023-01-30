import zdppy_requests as zr

response = zr.get("https://www.baidu.com/")
print(response.status_code)
print(response.text)

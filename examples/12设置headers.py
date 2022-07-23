import zdppy_requests

# 设置User-Agent浏览器信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'content-type': 'application/json'
}

# 设置请求头信息
response = zdppy_requests.get('https://www.zhihu.com/question/37787004', headers=headers)
print(response.text)

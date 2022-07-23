import zdppy_requests

response = zdppy_requests.get('http://l.bst.126.net/rsc/img/loginopen/201406/appstore/quanzi.jpg?v=001')

# 输出响应的二进制内容
print(response.content)

# 下载二进制数据到本地
with open('quanzi.jpg', 'wb') as f:
    f.write(response.content)
    f.close()

# zdppy_requests
基于requests二开的HTTP请求库，无任何第三方依赖，可独立使用，不受开源框架迭代的影响


# 使用示例
## 获取网页源码
```python
import zdppy_requests as zr

response = zr.get("https://www.baidu.com/")
print(response.status_code)
print(response.text)
```


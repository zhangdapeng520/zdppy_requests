from zdppy_requests import Requests

r = Requests(port=8080, debug=True)

r.log.info(r.upload("/test", "file", "z05_get_post_param.py").json())  # 自动解码

import time

"""web框架专门处理动态资源请求"""
def index():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # 响应体
    # 获取当前时间
    data = time.ctime()
    # 这里返回的是一个元组，括号可以省略
    return status, response_header, data

# 处理动态资源请求
def handle_request(env):
    # 获取动态资源请求路径
    request_path = env["request_path"]
    print("动态资源请求路径：", request_path)
    # 判断动态资源路径，选择指定函数处理对应的动态资源请求
    if request_path == "/index.html":
        # 获取首页数据
        result = index()
        # 把处理后的结果返回给web服务器，用于web服务器拼接响应报文使用
        return result

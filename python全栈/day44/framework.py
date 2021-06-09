import time

"""web框架专门处理动态资源请求"""

# 创建路由列表，每条记录是一个路由，由元组构成
# 装饰器在装饰时会自动添加路由到路由列表，所有路由列表为空就可以了
route_list = [
    # ("/index.html", index),
    # ("/center.html", center)
]


# 创建带有参数的装饰器
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器时就需要把路由添加到路由列表里面
        # 在装饰函数时添加一次路由即可
        route_list.append((path, func))
        def inner():
            result = func()
            return result
        return inner
    # 返回一个装饰器
    return decorator


@route("/index.html")
def index():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # 响应体
    # 1.打开指定模板文件，读取模板文件内容
    with open("template/index.html", "r") as file:
        file_data = file.read()
    # 2.查询数据库，替换模板中的变量（{%content%}
    # 获取当前时间,模拟数据库数据
    data = time.ctime()
    # 替换变量
    response_body = file_data.replace("{%content%}", data)
    # 这里返回的是一个元组，括号可以省略
    return status, response_header, response_body


@route("/center.html")
def center():
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # 响应体
    with open("template/center.html", "r") as file:
        file_data = file.read()

    # 这里返回的是一个元组，括号可以省略
    return status, response_header, file_data


def not_found():
    # 状态信息
    status = "404 Not Found"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # 响应体
    # 获取当前时间
    data = "NOT FOUND"
    # 这里返回的是一个元组，括号可以省略
    return status, response_header, data 


# 处理动态资源请求
def handle_request(env):
    # 获取动态资源请求路径
    request_path = env["request_path"]
    print("动态资源请求路径：", request_path)
    # # 判断动态资源路径，选择指定函数处理对应的动态资源请求
    # if request_path == "/index.html":
    #     # 获取首页数据
    #     result = index()
    #     # 把处理后的结果返回给web服务器，用于web服务器拼接响应报文使用
    #     return result
    # else:
    #     # 没有找到资源路径，返回404
    #     result = not_found()
    #     return result
    for path, func in route_list:
        if request_path == path:
            # 找到路由，执行对应的处理函数
            # print(request_path)
            result = func()
            # 将处理后的结果返回web服务，进行报文拼接
            return result
    else:
        # 没有资源数据，返回404
        result = not_found()
        return result
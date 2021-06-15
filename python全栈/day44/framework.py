import json
import pymysql

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

# 个人数据中心接口
@route("/center_data.html")
def center_data():
    # 从数据库中取数据，然后把数据转换成json格式
    # 创建数据库连接对象
    conn = pymysql.connect(host="192.168.33.13",
                            port=3306,
                            user="root",
                            password="123456",
                            database="stock_db",
                            charset="utf8")
    # 获取游标
    cursor = conn.cursor()
    # 准备sql
    sql = """
     select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info  
     from info i inner join focus f on i.id=f.info_id;
    """
    # 执行sql
    cursor.execute(sql)
    # 获取结果
    result = cursor.fetchall()
    print(result)
    # 将获得的元组转成列表字典
    center_data_list = [{
                            "code":row[0],
                            "short":row[1],
                            "chg":row[2],
                            "turnover":row[3],
                            "price":str(row[4]),
                            "highs":str(row[5]),
                            "note_info":row[6]
                        } for row in result]
    # print(center_data_list)
    # 把列表字典转换成json
    # 在控制台显示中文，ensure_ascci=False
    json_str = json.dumps(center_data_list, ensure_ascii=False)
    # print(json_str)
    # print(type(json_str))
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 页面访问
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1"), ("Content-Type", "text/html; charset=utf-8")]
    return status, response_header, json_str


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
    # 创建连接对象
    conn = pymysql.connect(host="192.168.33.13",
                            port=3306,
                            user="root",
                            password="123456",
                            database="stock_db",
                            charset="utf8")

    # 获取游标
    cursor = conn.cursor()
    # 准备sql
    sql = "select * from info;"
    # 执行sql
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    print(result)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    # 遍历每一条数据，完成数据的tr标签封装
    data = ""
    for row in result:
        data += """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><input type="button", value="添加", id="toAdd", name="toAdd"></td>
        </tr>
        """ % row

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

if __name__ == "__main__":
    center_data()
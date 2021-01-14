import socket
import os
import threading

# 处理客户端请求
def handle_client_request(new_socket):
    # 接受客户端请求信息
    recv_data = new_socket.recv(4096)
    # 判断请求数据是否为空，为空退出函数
    if len(recv_data) == 0:
        new_socket.close()
        return
    # 对接受数据进行二进制解码
    recv_content = recv_data.decode("utf-8")
    # 对数据进行分割
    request_list = recv_content.split(" ", maxsplit=2)
    # 获取请求的资源路径
    request_path = request_list[1]
    print(request_path)
    if request_path == "/":
        request_path = "/index.html"

    # 判断文件是否存在
    # 1.os.path.exits
    # if not os.path.exists("static"+request_path):
    #     print("static"+request_path+"not exist")
    #     return
    # 2.try-except
    try:
        # 打开文件读取数据 提示，这里使用rb模式，兼容打开图片文件
        with open("static"+request_path, "rb") as file:
            file_data = file.read()
    except Exception as e:
        # 代码执行到此，说明没有请求的文件，返回404
        # 响应行
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 响应头
        response_header = "Server: LRY/1.0\r\n"
        # 空行
        # 响应体
        with open("static/error.html", "rb") as file:
            file_data = file.read()
        response_body = file_data
        response = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        # response已经是二进制数据，不用再编码
        # # 把数据编码成二进制
        # response_data = response.encode("utf-8")
        # 发送http响应格式数据
        new_socket.send(response)

    else:
        # 代码执行到此，说明找到了请求文件,返回200
        # 将数据封装成http响应报文发送给浏览器客户端
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server: LRY/1.0\r\n"
        # 空行
        # 响应体
        response_body = file_data
        # 此时response_body是二进制，不能和字符串拼接，将前面字符串编码为二进制
        response = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        # response已经是二进制数据，不用再编码
        # # 把数据编码成二进制
        # response_data = response.encode("utf-8")
        # 发送http响应格式数据
        new_socket.send(response)
    finally:
        # 关闭服务端套接字服务
        new_socket.close()


def main():
     # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口
    tcp_server_socket.bind(("", 8000))
    # 设置监听
    tcp_server_socket.listen(128)
    # 循环等待客户端请求
    while True:
        # 等待接受客户端连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明连接建立成功
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket,))
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()
        
# 判断是否是主程序
if __name__ == "__main__":
    main()
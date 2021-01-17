import socket
import os
import threading
import sys

# http协议的web服务器类
class HttpWebServer(object):
    def __init__(self, port):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        # 把tcp服务器的套接字作为web服务器对象的属性
        self.tcp_server_socket = tcp_server_socket

    # 处理客户端请求
    # 用不到当前方法和当前类，使用静态方法，方法之间空一行，函数之间空两行
    @staticmethod
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
    
    # 启动服务器的方法
    def start(self):
        # 循环等待客户端请求
        while True:
            # 等待接受客户端连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 代码执行到此，说明连接建立成功
            # 使用对象来调用静态方法
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()
        



def main():
    # 获取终端命令行参数
    params = sys.argv
    if len(params) != 2:
        print("执行命令格式如下：python XXX.py 9000")
        return
    
    # 判断第二个参数是否时数字组成
    if not params[1].isdigit():
        print("执行命令格式如下：python XXX.py 9000")
        return
    
    # 代码执行到此，说明命令行参数个数一定是2并且都是数字
    port = int(params[1])
    
    # 创建web服务器
    web_server = HttpWebServer(port)
    # 启动服务器
    web_server.start()
# 判断是否是主程序
if __name__ == "__main__":
    main()
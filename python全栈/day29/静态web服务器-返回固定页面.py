import socket

# 判断是否是主程序
if __name__ == "__main__":
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
        # 接受客户端请求信息
        recv_data = new_socket.recv(4096)
        print(recv_data)

        # 打开文件读取数据
        with open("index.html", "r") as file:
            file_data = file.read()

        # 将数据封装成http响应报文发送给浏览器客户端
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server: LRY/1.0\r\n"
        # 空行
        # 响应体
        response_body = file_data
        response = response_line + response_header + "\r\n" + response_body
        # 把数据编码成二进制
        response_data = response.encode("utf-8")
        # 发送http响应格式数据
        new_socket.send(response_data)
        # 关闭服务端套接字服务



import socket

if __name__ == "__main__":

    # 1.创建服务端套接字对象
    # AF_INET:IPV4
    # SOCKET_STREAM:tcp
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用，即程序结束后立即释放端口号，默认占用2分钟
    # SOL_SOCKET: 当前socket
    # SO_RESUERADDR: 复用端口号选项
    # True：启用端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2.绑定端口号
    # 传入一个元组对象，包括两个参数，ip和端口号
    # ip一般不用指定，表示本机任何一个网口都行
    tcp_server_socket.bind(("", 9090))
    
    # 3.设置监听
    # 128表示最大等待建立的连接数
    tcp_server_socket.listen(128)

    # 4.等待客户端链接请求
    # 注意：每次客户端与服务端建立连接成功都会产生一个新的套接字
    # tcp_server_socket这个套接字只负责等待接受客户端的连接请求，不负责收发消息
    new_client, ip_port = tcp_server_socket.accept()
    # 代码执行到此，说明客户端与服务段已经建立了连接
    print("客户端的ip和端口号为：",ip_port)
    
    # 5.接受客户端数据
    # 收发消息使用返回的新套接字
    recv_data = new_client.recv(1024)
    # 对二进制数据进行解码
    recv_content = recv_data.decode("utf-8")
    print("收到的消息为：", recv_content)

    # 6.发送数据到客户端
    send_content = "问题正在处理中。。。"
    send_data = send_content.encode("utf-8")
    new_client.send(send_data)

    # 7.关闭套接字
    # 首先关闭服务端与客户端套接字，表示和客户端连接中断
    new_client.close()
    # 再关闭服务端套接字，表示服务端不再接受客户端连接请求
    tcp_server_socket.close()
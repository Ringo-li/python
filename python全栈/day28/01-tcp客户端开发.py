import socket

#判断这段代码是不是主模块,是则加main判断，好处：
#1.别人导入时不执行
#2.防止创建多进程时无限制创建多进程
if __name__ == "__main__":
    #1.创建tcp客户端套接字
    #AF_INET：IPV4地址类型
    #SOCK_STREAM：TCP传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2.和服务器端套接字建立链接
    tcp_client_socket.connect(("192.168.33.150", 9090))

    #3.发送数据到服务端
    send_content = "你好，我是客户端"
    #将字符串编码成为二进制
    #windows编码为gbk,linux编码为utf-8
    send_data = send_content.encode("utf-8")

    tcp_client_socket.send(send_content)

    #4.接受服务端数据
    #1024：接收数据的最大字节数
    recv_data = tcp_client_socket.recv(1024)
    #对数据进行解码
    recv_content = recv_data.decode("utf-8")
    print(recv_content)

    #5.关闭套接字
    tcp_client_socket.close()
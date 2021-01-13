#!/usr/bin/env python
# -*- coding: utf8 -*-
import socket

# 判断这段代码是不是主模块,是则加main判断，好处：
# 1.别人导入时不执行
# 2.防止创建多进程时无限制创建多进程
if __name__ == "__main__":
    # 1.创建tcp客户端套接字
    # AF_INET：IPV4地址类型
    # SOCK_STREAM：TCP传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口号复用，即程序结束后立即释放端口号，默认占用2分钟
    # SOL_SOCKET: 当前socket
    # SO_RESUERADDR: 复用端口号选项
    # True：启用端口号复用
    tcp_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 客户端不强制要求绑定端口号
    tcp_client_socket.bind(("", 8900))
    

    # 2.和服务器端套接字建立链接
    tcp_client_socket.connect(("192.168.1.7", 9090))

    # 3.发送数据到服务端
    send_content = u"你好，我是客户端"
    # python2还要加u
    # send_content = u"你好，我是客户端"
    # 将字符串编码成为二进制
    # windows编码为gbk,linux编码为utf-8
    send_data = send_content.encode("utf-8")

    tcp_client_socket.send(send_data)

    # 4.接受服务端数据
    # 1024：接收数据的最大字节数
    recv_data = tcp_client_socket.recv(1024)
    # 对数据进行解码
    recv_content = recv_data.decode("utf-8")
    print(recv_content)

    # 5.关闭套接字
    tcp_client_socket.close()
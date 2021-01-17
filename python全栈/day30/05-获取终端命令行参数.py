import sys

# 获取终端命令行参数
params = sys.argv
print(params, type(params))

# 在终端执行
# [root@centos76 ~]# python3 python_learning/day29/05-静态web服务器-获取终端命令行参数.py 9000

# 列表中的每项都是字符串
# ['python_learning/day29/05-静态web服务器-获取终端命令行参数.py', '9000'] <class 'list'>
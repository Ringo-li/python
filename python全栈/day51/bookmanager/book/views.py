from os import name
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
# 视图
# 1.就是python函数
# 2.函数的第一个参数是请求，和请求相关的HttpRequest实例对象
# 3.必须返回一个响应，响应是HttpResponse实例对象

def index(request):
    # render参数：request, template_name, context=None
    # 第一个参数，当前请求
    # 第二个参数，模板文件
    # 第三个参数，context传递参数

    name = '如花'
    context = {
        'name': name
    }
    return render(request, 'index.html', context)
    return HttpResponse('index')

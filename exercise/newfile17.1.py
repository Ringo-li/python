try:
    n=input("请输入一个数字:")
    assert n.isdigit(),"只能输入正整数" #断言后抛出异常
    print("你输入的是：",n)
except Exception as a: #把抛出的异常赋值给a
    print("发现错误:",a)

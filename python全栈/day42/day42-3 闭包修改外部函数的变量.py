def func_out():
    num1 = 10
    def func_inner():
        # num1 = 20 只是在闭包内定义了一个局部变量，并没有修改外部函数变量
        # global num1，也无法修改，因为global是修改全局变量的
        # 使用关键字nolocal来修改外部函数变量
        nonlocal num1
        num1 = 20
        result = num1 + 10
        print("闭包执行结果：", result)
    
    print("外部变量修改前：", num1)
    func_inner()
    print("外部变量修改后：", num1)
    return func_inner

new_func = func_out()
new_func()
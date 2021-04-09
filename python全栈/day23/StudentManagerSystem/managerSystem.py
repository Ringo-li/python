from student import *

"""
需求：
    1.能够存储数据
        数据文件（student.data），数据格式:list
    2. 功能系统
        增删改查，显示全部，保存数据
"""

class ManagerSystem(object):
    """
    功能系统循环使用，用户输入不同序号执行不同功能。
    """

    # 初始化
    def __init__(self):
        # 存储数据的列表
        self.student_list = []

    # 一、入口函数，启动程序后执行的函数
    def run(self):
        """
        加载数据
        显示功能菜单
        用户输入功能序号
        根据序号执行不同功能
        """
        
        # 加载学员信息
        self.load_students()
        

        while True:
            # 显示功能菜单
            self.show_menu()
            

            # 用户输入功能序号
            menu_num = int(input("用户输入功能序号:"))

            # 根据序号执行功能
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    # 二、功能函数
    # 2.1显示功能菜单 --打印功能和序号对应关系，不涉及对象和对象数据的使用
    # 不需要每个对象有自己的显示方式， --静态以节省资源
    @staticmethod
    def show_menu():
        print("-" * 20)
        print("请选择如下功能：")
        print("1：添加学员")
        print("2：删除信息")
        print("3：修改信息")
        print("4：查询信息")
        print("5：显示所有信息")
        print("6：保存信息")
        print("7：退出")
        print("-" * 20)

    # 2.2添加学员
    def add_student(self):
        # 1.用户输入姓名、性别、电话
        name = input("请输入姓名：")
        gender = input("性别：")
        tel = input("电话：")
        
        # 2.创建学员对象
        student = Student(name, gender, tel)

        # 3.将该对象添加到学员列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 2.3删除学员
    def del_student(self):
        # 1.用户属于要删除的学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # 2.如果学名姓名存在，则删除，不存在，则提示无此人
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        # 循环代码正常执行完毕，说明没有删除的对象
        else:
            print("查无此人")

        # 打印学员列表，验证删除功能
        print(self.student_list)

    # 2.4修改学员信息
    def modify_student(self):
        # 1.用户输入学名姓名
        modify_name = input('请输入需要修改的学员姓名：')

        # 2.遍历列表，如果存在需要修改的学员则修改姓名、性别和电话，不存在提示信息
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('name:')
                i.gender = input('gender:')
                i.tel = input('tel:')
                print('学员信息修改完毕。姓名：{}，性别：{}，电话：{}'.format(i.name, i.gender, i.tel))
                break
        else:
            print('学员不存在')

    # 2.5查询信息
    def search_student(self):
        # 1.用户输入学员信息
        search_name = input('请输入查询的学员姓名：')

        # 2.遍历学员列表，存在则按格式显示信息，不存在提示并退出
        for i in self.student_list:
            if search_name == i.name:
                print('name:{}, gender:{}, tel:{}'.format(i.name, i.gender, i.tel))
                break
        else:
            print('学员不存在')

    # 2.6显示所有学员信息
    def show_student(self):
        # 1.打印表头
        print('姓名\t性别\t电话')
        # 2.遍历打印学员信息
        for i in self.student_list:
            print('{}\t{}\t{}'.format(i.name, i.gender, i.tel))

    # 2.7保存信息
    def save_student(self):
        # 1.打开文件
        data_file = open('student.data', 'w')
        # 2.写入学员信息
        # 2.1学员对象转换成字典
        new_list = [i.__dict__ for i in self.student_list]
        # 2.2文件写入必须是字符串格式
        data_file.write(str(new_list))
        # 3.关闭文件
        data_file.close()

    # 2.8加载学员信息
    def load_students(self):
        # 1.打开文件：尝试r模式打开学员信息文件，如有报错则新建w
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')

        # 2.读取文件：格式转换，先将字符串转换为字典，再将字典转换为对象
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        # 3.关闭文件
        finally:
            f.close()
    



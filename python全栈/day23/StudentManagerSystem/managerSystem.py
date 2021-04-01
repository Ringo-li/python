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
                self.search_student  
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    # 二、功能函数
    # 2.1显示功能菜单 --打印功能和序号对应关系，不需要每个对象有自己的显示方式， --静态以节省资源
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
        print("增加学员信息")

    # 2.3删除学员
    def del_student(self):
        print("删除信息")

    # 2.4修改学员信息
    def modify_student(self):
        print("修改信息")

    # 2.5查询信息
    def search_student(self):
        print("查询信息")

    # 2.6显示所有学员信息
    def show_student(self):
        print("显示所有信息")

    # 2.7保存信息
    def save_student(self):
        print("保存信息")

    # 2.8加载学员信息
    def load_students(self):
        print("加载学员信息")
    



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

    # 入口函数
    def run(self):
        """
        加载数据
        显示功能菜单
        用户输入功能序号
        根据序号执行不同功能
        """
        
        # 加载学员信息
        print("加载学员信息")

        while True:
            # 显示功能菜单
            print("显示功能菜单")

            # 用户输入功能序号
            menu_num = int(input("用户输入功能序号:"))

            # 根据序号执行功能
            if menu_num == 1:
                print("增加信息")
            elif menu_num == 2:
                print("删除信息")
            elif menu_num == 3:
                print("修改信息")
            elif menu_num == 4:
                print("查询信息")
            elif menu_num == 5:
                print("显示所有信息")
            elif menu_num == 6:
                print("保存信息")
            elif menu_num == 7:
                break

    # 功能函数
    
    

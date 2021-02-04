def print_info():
    print('\n' + '-' * 35)
    print('请输入对应数字执行操作:')
    print('1.增加学员')
    print('2.删除学员')
    print('3.修改学员信息')
    print('4.查询所有学员')
    print('5.显示所有学员信息')
    print('6.退出系统')
    print('-' * 35 + '\n')

def add_info():
    """
    添加学员信息
    """
    new_id = input('学号：')
    for i in info:
        if i['学号'] == new_id:
            print('学号已经存在')
            # return退出当前函数，让后面的添加操作不执行
            return
    new_name = input('姓名：')
    new_tel = input('电话：')



    new_info= {}
    new_info['学号'] = new_id
    new_info['姓名'] = new_name
    new_info['电话'] = new_tel

    info.append(new_info)
 
def del_info():
    """删除学员信息"""
    del_id = input('请输入删除学员学号:')
    for i in info:
        if del_id == i['学号']:
            info.remove(i)
            print('学员{}已经删除'.format(i['姓名']))
            # 当匹配成功后不用再往下遍历了，所有用break中断循环，
            # 但如果没有匹配到，应该打印一个未找到的信息，
            # 我们可以为for加else语句，在循环正常结束时执行，满足要求
            break
    else:
        print('没有找到这个学号')

def modify_info():
    """修改学员信息"""
    modify_id = input('请输入要修改的学号：')
    for i in info:
        if modify_id == i['学号']:
            # i['学号'] = input('请输入新学号：')
            # i['姓名'] = input('请输入新姓名：')
            i['电话'] = input('请输入新电话：')
            print('{}信息已经修改'.format(i['学号']))
            break
    else:
        print('没有找到这个学号')

def query_info():
    """查询学员信息"""
    query_name = input('请输入学员姓名：')
    num = 0
    for i in info:
        if i['姓名'] == query_name:
            num += 1
            print('学员{}信息：'.format(num))
            print('{name}的学号：{id}，电话：{tel}'.format(name=i['姓名'], id=i['学号'], tel=i['电话']))
    print('共找到{}个同名学员'.format(num))

def print_all():
    """打印所有学员信息"""
    print('\n\t姓名\t学号\t电话')
    for i in info:
        print('\t{name}\t{id}\t{tel}'.format(name=i['姓名'], id=i['学号'], tel=i['电话']))

info = []
while True:
    print_info()
    try:
        choice_num = int(input('请输入选项:'))
    except Exception as e:
        print('请输入对应数字')
        continue
    if choice_num == 1:
        # print('增加')
        add_info()
    elif choice_num == 2:
        # print('删除')
        del_info()
    elif choice_num == 3:
        # print('修改')
        modify_info()
    elif choice_num == 4:
        # print('查询')
        query_info()
    elif choice_num == 5:
        # print('显示所有')
        # print(info)
        print_all()
    elif choice_num == 6:
        exit_flag = input('确定要退出吗？(y/n):')
        if exit_flag == 'y':
            break
    else:
        print('请输入正确选项')
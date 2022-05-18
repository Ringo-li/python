# 输入 1/N 2/Y 3/N 4/N 5/N 6/Y
# 有两个幼儿园班级，2/Y 表示第二个小朋友和前一个是同一个班，反之不是同一个班
# 班级排序：谁的第一个学号更小，小朋友排序：从小到大
# 如一个班级为空，输出空行

try:
    s = input().split()
    lst = []
    first = []
    second = []
    for i in s:
        lst.append(i.split('/'))
    for i in range(len(lst)):
        if int(lst[i][0]) < 0 or int(lst[i][0]) > 999:
            raise 
        if lst[i][1] == 'N':
            first, second = second, first
        first.append(int(lst[i][0]))
    first.sort()
    second.sort()
    if len(second) ==0:
        print(' '.join(map(str,first)))
        print('')

    elif first[1] > second[1]:
        first, second = second,first
        print(' '.join(map(str,first)))
        print(' '.join(map(str,second)))
    else:
        print(' '.join(map(str,first)))
        print(' '.join(map(str,second)))
except:
    print('ERROR')
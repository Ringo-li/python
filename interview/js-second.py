# 题目：第一行输入vlan格式如20-21,15,18,19,30,31,5-10
# 第二行输入要删除的vlan，比如 15
# 输出剩余vlan，其格式5-10,18-21,30-31,连续则省略


# s = "20-21,15,18,19,30,31,5-10"
# n = 15
# s = '1-5'
# n = 2
s = input()
n = int(input())
lst = []
if ',' in s:
    s = s.split(',')
    for i in s:
        if '-' in i:
            tmp = i.split('-')
            for j in range(int(tmp[0]), int(tmp[1])+1):
                lst.append(j)
        else:
            lst.append(int(i))
else:
    tmp = s.split('-')
    for j in range(int(tmp[0]), int(tmp[1])+1):
        lst.append(j)

lst.remove(n)
lst.sort()

path = ''
for i in range(len(lst)-1):
    if lst[i] == lst[i-1]+1:
        path += str(lst[i])+ ' '
    else:
        path += ','
        path += str(lst[i])+ ' '


if len(lst) == 1:
    print('')
elif len(lst) >= 2:
    if lst[-1] == lst[-2]+1:
        path += str(lst[-1])
    else: 
        path += ','
        path += str(lst[-1])

    result = []
    path = path.split(',')
    for i in path:
        if len(i) == 0:
            pass
        else:
            tmp = i.split()
            if len(tmp) >= 2:
                result.append(tmp[0] + '-' + tmp[-1]) 
            # elif len(tmp) == 2:
            #     result.append(tmp[0]+','+tmp[1])
            else:
                result.append(tmp[0])
    print(','.join(result))

# print(path)


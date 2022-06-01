n = int(input())
if 1 <= n <= 10**8:
    lst = list(str(n))
    lst.reverse()
    tmp = []
    for i in lst:
        if i not in tmp:
            tmp.append(i)
    tmp.reverse()
    sum = 0
    for j in range(len(tmp)):
        sum += int(tmp[j])*10**j
    print(sum)


n = input()
if 1 <= int(n) <= 10**8:
    n = n[::-1]
    num=[]
    for i in n:
        if i in num:
            continue
        else:
            num.append(i)
            print(i,end='')




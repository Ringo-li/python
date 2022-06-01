while True:
    try:
        n, k = input().split()
        lst = [int(i) for i in input().split()]
        lst.sort()
        print(" ".join(map(str, lst[0:k])))
    except:
        break

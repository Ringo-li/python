a = float(input())
if a <= 0:
    print('大于0')
elif a >= 2**32:
    print('too large')
else:
    if a%1 >= 0.5:
        print(int(a//1)+1)
    else:
        print(int(a//1))

# #思路2
# n = float(input())
# if n - int(n) >= 0.5:
#     print(int(n)+1)
# else:
#     print(int(n))
#
# #思路3
# n = float(input())
# y = lambda x : int(x+0.5)
# print(y(n))


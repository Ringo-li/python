alist = ['abc','b','ab','aabb']
a = sorted(alist,key=lambda x:len(x),reverse=True)
print(a)
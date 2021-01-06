#copy和deepcopy区别
import copy
#不可变对象str set
astr = '哇哈哈'

a = copy.copy(astr)
b = copy.deepcopy(astr)
print(astr,id(astr))
print(a,id(a))
print(b,id(b))

#简单可变对象list dict
adict = {'one':1,'two':2}

a = copy.copy(adict)
b = copy.deepcopy(adict)
print(adict,id(adict))
print(a,id(a))
print(b,id(b))

adict['two'] = 3
print(adict,id(adict))
print(a,id(a))
print(b,id(b))

#复杂可变对象

alist = [1,2,[3,4]]

a = copy.copy(alist)
b = copy.deepcopy(alist)
print(alist,id(alist))
print(a,id(a))
print(b,id(b))

alist[1] = 0
print(alist,id(alist))
print(a,id(a))
print(b,id(b))

alist[2][1] = 5
print('alist的子列表发生变化后',alist,id(alist))
print('a不是真正的复制',a,id(a))
print('b是真正的复制',b,id(b))
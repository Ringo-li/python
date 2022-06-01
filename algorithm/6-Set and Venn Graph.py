# set, 也是一种数据结构，it's a collection but only  with the unique data
# 韦恩图，两个相交的集合
# 例题，判断字符串中是否有重复元素

string = 'a a b c d'
# 方法一
def f(s):
    lst = list(s.split())
    if len(lst) > len(set(lst)):
        return True
    else:
        return False
    
print(f(string))
# 方法二
def f(s):
    st = set()
    for i in list(s.split()):
        if i in st:
            return True
        else:
            st.add(i)
    return False

print(f(string))






A = set([1,2,3])
B = set([3,4,5])

# 添加和删除元素
A.add(4)
B.remove(3)

print(A & B)
print(A.intersection(B))

print(A | B)
print(A.union(B))

print(A ^ B)
print(A.symmetric_difference(B))

print(A - B)

# 判断连个集合是否没有交集
print(A.isdisjoint(B))
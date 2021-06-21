import copy

# 不可变类型:元组/字符串/数字
str1 = "wahaha"
# copy()浅拷贝函数
str2 = copy.copy(str1)
print("str1:", id(str1), "str2:", id(str2))

tuple1 = (1, 3, 5)
tuple2 = copy.copy(tuple1)
print("tuple1:", id(tuple1), "tuple2:", id(tuple2))
#
# 浅拷贝不会改变不可变类型的内存地址 

# 可变类型
list1 = [1, 3, [5, 7]]
list2 = copy.copy(list1)
print("list1:", id(list1), "list2:", id(list2))
list1.append(9)
print("list1:", list1, "list2:", list2)
list1[2].append(9)
print("list1:", list1, "list2:", list2)
print("list1[2]:", id(list1[2]), "list2[2]:", id(list2[2]))

# 浅拷贝会改变可变类型的内存地址,但是不会改变子对象的内存地址
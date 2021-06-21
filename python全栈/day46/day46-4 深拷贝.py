import copy

# copy.deepcopy()深拷贝
# 不可变类型不能改变内存地址,能改变内存地址就不是不可变类型
num1 = 1
num2 = copy.deepcopy(num1)
print("num1:", id(num1), "num2:", id(num2))

# 元组时不可变类型,但是当元组中还有可变类型数据,也会改变内存地址
# 只有在对象内部发现可变类型,都会改变内存地址
tuple1 = (1, 3, [5, 7])
tuple2 = copy.deepcopy(tuple1)
print("tuple1:", id(tuple1), "tuple2:", id(tuple2))
print("tuple1[2]:", id(tuple1[2]), "tuple2:", id(tuple2[2]))
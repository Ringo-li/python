# 对列表中的字典按照某一个key值进行排序
# 对于每个对象有不同属性，多个对象组成一个组合的情况，可以适用

students = [
    {'name':'Tom', 'age':18},
    {'name':'Rose', 'age':16},
    {'name':'Jack', 'age':17}
]

# 按name值升序排序
students1 = students.copy()
students1.sort(key=lambda x: x['name'])
print(students1)

# 按name值降序排序
students2 = students.copy()
students2.sort(key=lambda x: x['name'], reverse=True)
print(students2)

# 按age值降序排列
students3 = students.copy()
students3.sort(key=lambda x: x['age'], reverse=True)
print(students3)
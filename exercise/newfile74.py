foo = [{"name":"zs","age":19},{"name":"IV","age":54},{"name":"wa","age":17},{"name":"rlf","age":34}]
print(foo)
a = sorted(foo,key=lambda x:x["age"],reverse=True)
print(a)

a = [i for i in foo if i['age'] < 30]
print(a)
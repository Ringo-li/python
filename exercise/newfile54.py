import re
a = 'jdjcjdj3465mckfnnf4522~fncndk'
b = re.findall(r'\d+',a)
print(b)

sub1 = re.sub(r'\d+','num',a)
print(sub1)

a = "%.3f"%1.335
print(a,type(a))
b = round(float(a),1)
print(b)
b = round(float(a),2)
print(b)


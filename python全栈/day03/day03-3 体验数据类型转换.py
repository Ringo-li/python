dct = '{"a":2, "b":3}'
print(dct)
print(eval(dct)['a'])


a = '''{
  'foo': "fighter",
  'bar': [1,2,3]
}'''

print(type(a))
print(eval(a)['bar'])
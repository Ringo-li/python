alist = ['中国','Barli','England','保加利亚','',' ','梵蒂冈']

res1 = list(map(lambda x:'wahahs' if x == '' or x == ' ' else x,alist))
res2 = list([ i for i in alist if i != '' or i != ' ' ])
print(res1)
print(res2)

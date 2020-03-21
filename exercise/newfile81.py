
name = input('please input your name:')
sql = 'select * from dome where name="%s"' % name

print(sql)

name = 'zr;drop database demo'
sql = 'select * from dome where name="%s"' % name
print(sql)

name = 'zr;drop database demo'
initname = [name]
#csl = 'connect mysqldb successful:'.cursor()
#sql = csl.excute('select * from dome where name="%s"',initname)
sql = 'select * from demo where name = %s'%initname
print(sql)
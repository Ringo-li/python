import pymysql

conn = pymysql.connect(host='192.168.33.13',
                        port=3306,
                        database='students',
                        charset='utf8',
                        user='root',
                        password='mysql'
                    )

cursor = conn.cursor()
# 可以查询所有信息的sql注入
# sql = "select * from students where name='%s'" %"李四' or 1 = 1 or '"
# cursor.execute(sql)
# resault = cursor.fetchall()
# print(resault)

# sql语句参数化，使用防止注入的sql语句，%s是sql语句的参数，和python字符串中的%s占位符不一样，不要加引号
sql = "select * from students where name=%s"

# 执行sql，加入参数,元组格式，可以防止注入
# cursor.execute(sql,("李四' or 1 = 1 or '",))
cursor.execute(sql,("李四",))
resault = cursor.fetchall()
print(resault)

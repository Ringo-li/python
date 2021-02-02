import pymysql
conn = pymysql.connect(host = '192.168.33.13',
                        port = 3306,
                        user = 'root',
                        database = 'students',
                        password = 'mysql',
                        charset = 'utf8'
                        )

cursor = conn.cursor()
sql = "update students set weight=135 where name='李四';"

try:
    # 执行sql
    cursor.execute(sql)
    # 提交修改的数据到数据库
    conn.commit()
except Exception as e:
    # 对修改的数据进行撤销，回到没有修改之前的状态
    conn.rollback()
    print(e)
finally:
    cursor.close()
    
    conn.close()
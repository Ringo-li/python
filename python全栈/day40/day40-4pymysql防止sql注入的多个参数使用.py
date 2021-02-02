import pymysql

conn = pymysql.connect(host = "192.168.33.13",
                        port = 3306,
                        database = "students",
                        user = "root",
                        password = "mysql",
                        charset = "utf8"
                        )

cursor = conn.cursor()
sql = "insert into students (name, age, gender) values (%s, %s, %s);"

try:
    # 执行sql，传入参数，多个参数可以是元组、字典、列表
    cursor.execute(sql,["司马", 35, "男"])
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
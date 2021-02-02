# 1.导入包
import pymysql

if __name__ == "__main__":
    # 2.创建连接对象

    conn = pymysql.connect(host="192.168.33.13",
                            port = 3306,
                            user = 'root',
                            password = 'mysql',
                            database =  'students',
                            charset = "utf8")

    # 3.获取游标，目的是执行sql语句
    cursor = conn.cursor()

    # 4.执行sql语句
    # 4.1准备sql语句
    sql = "select * from students;"
    # 4.2执行sql语句
    cursor.execute(sql)
    # 4.3获取第一条查询结果,类型是元组
    # row = cursor.fetchone()
    # print(row)
    # 4.4获取多条返回结果,元组套元组格式
    result = cursor.fetchall()
    # print(result)
    for row in result:
        print(row)

    # 5.关闭游标
    cursor.close()

    # 6.关闭连接
    conn.close()

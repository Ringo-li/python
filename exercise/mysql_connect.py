# -*- coding: utf-8 -*-
import MySQLdb
try:
  conn=MySQLdb.connect(host='192.168.65.146',port=3306,db='student',user='root',passwd='toor',charset='utf8')
  csl=conn.cursor()
  count=csl.execute("insert into stu(stu_id,stu_name,stu_phone,stu_hometown) values('0003','kj','19564832601',河北)")
  print(count)
  conn.commit()
  csl.close()
  conn.close()
except Exception as e:
  print (e)
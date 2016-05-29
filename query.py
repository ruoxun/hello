# -*- coding:UTF-8 -*-

import psycopg2
# 注册字符串缺省类型为unicode
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

# Connect to an existing database


conn = psycopg2.connect(host='localhost', 
	database="hw04", user="dbo", password="123456")


with conn.cursor() as cur:
	sql = '''
	SELECT sn, name
    FROM hw_a
        SELECT sn, name
    FROM hw_b
   
        LEFT OUTER JOIN  ON hw_a.sn = hw_b.sn;
        LEFT OUTER JOIN  ON hw_a.name = hw_b.name;
	'''
	cur.execute(sql)
	for row in cur: 

		print (row[0], row[1])

conn.commit()


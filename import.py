# -*- coding:UTF-8 -*-

import psycopg2

# Connect to an existing database


conn =psycopg2 .connect(host='localhost', 
	database="hw04", user="dbo", password="123456")

cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a  (
    sn       INTEGER,    --序号
    name     TEXT        --姓名
);
	''')


cur.execute('''
		INSERT INTO hw_a (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':10, 'name':A10} )
cur.execute('''
		INSERT INTO hw_a (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':20, 'name':A20} )

cur.execute('''
		INSERT INTO hw_a (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':30, 'name':A30} )

cur.execute('''
		INSERT INTO hw_a (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':40, 'name':A40} )

cur.execute('''
		INSERT INTO hw_a (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':50, 'name':A50} )

cur.execute('''
		INSERT INTO hw_a (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':60, 'name':A60} )


conn.commit()









cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b  (
    sn       INTEGER,    --序号
    name     TEXT        --姓名
);
	''')


cur.execute('''
		INSERT INTO hw_b (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':40, 'name':B40} )
cur.execute('''
		INSERT INTO hw_b (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':50, 'name':B50} )

cur.execute('''
		INSERT INTO hw_b (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':60, 'name':B60} )

cur.execute('''
		INSERT INTO hw_b (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':70, 'name':B70} )

cur.execute('''
		INSERT INTO hw_b (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':80, 'name':B80} )


conn.commit()

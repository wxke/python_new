#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import pymysql

conn =pymysql.connect(host='127.0.0.1',port = 3306,user='root',passwd='123456',db='student')
cursor = conn.cursor()

effect_row = cursor.execute('select * from test')
conn.commit()
print(cursor.fetchall())
cursor.close()
conn.close()
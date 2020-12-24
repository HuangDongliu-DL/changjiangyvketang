#coding=utf-8
import json
import sqlite3

conn = sqlite3.connect("../Question_Bank.db")
c = conn.cursor()
Data = json.load(open('./mayuan.json',encoding='utf-8'))

for i in Data:
    Q = i['Description']
    answer = i['Answer']
    A_str = ''
    for j in answer:
        A_str += i['Choice'][ord(j)-65].replace('A','').replace('.','').replace('B','').replace('C','').replace('D','') + "&"
    SQL = "INSERT INTO Data VALUES (?,?)"
    c.execute(SQL, (Q, A_str))
    conn.commit()
conn.close()
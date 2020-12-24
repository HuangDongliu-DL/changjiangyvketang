#coding=utf-8
import json
import sqlite3

def Get_data():
    '''第七章和其他的不一样特地写一个函数用来提取数据'''
    Data = json.load(open('./第七章试卷.json','r',encoding='utf-8'))
    conn = sqlite3.connect('Question_Bank.db')
    c = conn.cursor()
    SQL = "INSERT INTO Data VALUES (?,?)"
    for i in Data['data']['problems']:
        Q = i['Body'].replace('</p>','').replace("<p>","").replace('\n','')
        A = ''
        for o in i['Options']:
            for j in i['Answer']:
                if o['key'] == j:
                    A += o['value'].replace('</p>','').replace("<p>","") + "&"
        c.execute(SQL, (Q, A))
        conn.commit()
    conn.close()


Get_data()
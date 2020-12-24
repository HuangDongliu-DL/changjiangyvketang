#coding=utf-8
import sqlite3
import pandas as pd

class Question_Bank:
    '''
    创建一个题库
    '''
    def __init__(self):
        pass
    def create_sql(self):
        '''创建题库所需要的数据库'''
        # connect to sqlite
        conn = sqlite3.connect("Question_Bank.db")
        # c is cursor of sqlite
        c = conn.cursor()
        SQL = '''
            CREATE TABLE Data (Question TEXT NOT NULL,Answare TEXT NOT NULL)
         '''
        c.execute(SQL)
        conn.commit()
        conn.close()
    def insert_data(self):
        conn = sqlite3.connect('Question_Bank.db')
        c = conn.cursor()
        Data = pd.read_csv('./第五章.CSV',encoding='GBK')
        for i in Data.values:
            # 问题
            Q = i[2]
            A = ''
            for j in i[1]:
                A += i[ord(j)-62] + "&"
            SQL = "INSERT INTO Data VALUES (?,?)"
            c.execute(SQL,(Q,A))
            conn.commit()
        conn.close()

    def SQL_to_Word(self):
        conn = sqlite3.connect('Question_Bank.db')
        c = conn.cursor()
        c.execute("SELECT * from Data")
        D = ''
        for i in c.fetchall():
            A = i[0]
            Q = i[1]
            D += A + "\n"
            D += Q + "\n"
            D += "*****************************************" + '\n'
        with open('Answer.txt','w',encoding='utf-8') as f:
            f.write(D)

Q = Question_Bank()
Q.SQL_to_Word()
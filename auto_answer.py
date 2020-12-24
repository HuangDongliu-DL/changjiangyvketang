#coding=utf-8
#Author = HuangDongliu
#Start_time：2020、12、20
#Finally_time: 2020、12、21
import requests
import difflib
import json
import sqlite3
import time

class Auto_answer:
    '''
    需要考试的id号与验证身份的X_access_token
    '''
    def __init__(self):
        self.x_access_token = None
        self.class_id = None
        self.exam_id = None
        self.HEADERS = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
                        'Sec-Fetch-Dest': 'image',
                        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                        'Sec-Fetch-Site': 'same-site',
                        'Sec-Fetch-Mode': 'no-cors',
                        'Referer': 'https://www.yuketang.cn/v2/web/quizSummary/3545590/878580',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        }
        # 创建Session对象
        self.session = requests.session()
        # 题目数据URL
        self.PROBLEM_URL = "https://changjiang-exam.yuketang.cn/exam_room/show_paper?exam_id="
        # 提交数据的URL
        self.post_data_URL = "https://changjiang-exam.yuketang.cn/exam_room/answer_problem"

    def get_parme(self):
        '''
        获取必要的参数
        '''
        self.exam_id = input("Place input exam_id:")
        self.x_access_token = input("Place input x_access_token:").split('=')[-1]
        print("The program has started running, please wait for the result。。。。。。。。。。")
    def get_equal_rate_1(self,str1, str2):
        '''用于对比两端字符串的相似度'''
        return difflib.SequenceMatcher(None, str1, str2).quick_ratio()
    def Process_exam_data(self):
        # 再获取试卷时候必须要获取X-access-token
        URL = self.PROBLEM_URL+str(self.exam_id)
        Exam_data = self.session.get(
            URL,
            cookies={'x_access_token':self.x_access_token}
        ).json()
        #开始连接数据库
        conn = sqlite3.connect('./Question_Bank.db')
        c = conn.cursor()
        for i in Exam_data['data']['problems']:
            # 这个是问题字符串
            Q = i['Body'].replace('</p>', '').replace("<p>", "").replace('\n', '')
            # 这个是答案以词典保存
            A = {}
            # 这个是试题的编号
            problem_id = i['ProblemID']

            print("问题是：%s"%Q)
            for o in i['Options']:
                key = o['key']
                value = o['value']
                A[key] = value
            c.execute('SELECT * FROM Data')
            # 结果选项
            Result_options = []
            # 最佳匹配问题
            Best_question = ''
            # 最佳匹配结果
            Best_answer = ''
            # 字符串匹配的最大指数
            max_index = 0
            # 这里面Q表示试卷中的问题，q表示数据库中的问题数据
            for (q,a) in c.fetchall():
                index = self.get_equal_rate_1(Q,q)
                if index > max_index:
                    max_index = index
                    Best_question = q
                    Best_answer = a
            Best_answer_list = Best_answer.split('&')
            Answer_number = len(Best_answer_list)

            for (k, v) in A.items():
                Tem = []
                for a_item in Best_answer_list:
                    Tem.append(self.get_equal_rate_1(v, a_item))
                A[k] = max(Tem)

            A = sorted(A.items(), key=lambda A: A[1], reverse=True)
            print(A)


            for i in range(Answer_number - 1):
                Result_options.append(A[i][0])

            print("答案是：%s"%Result_options)
            print(Best_answer)
            print("***********************")

            # 构建自动答题的数据包
            Post_data = {"results":
                            [{"problem_id":problem_id,
                             "result":Result_options,
                             "time":int(time.time()*1000)
                             }],
                         "exam_id":self.exam_id,
                         "record":[]
                         }
            # 自动答题数据包的头信息
            Post_Headers = {
                'Content-Length': str(len(str(Post_data))),
                'Content-Type': 'application/json;charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60',
                }
            requests.post(url=self.post_data_URL, headers=Post_Headers,cookies={'x_access_token':self.x_access_token} ,data=json.dumps(Post_data))
            time.sleep(0.3)
# 实例化自动答题对象
A = Auto_answer()
# 获取参数信息
A.get_parme()
# 获取并写入答案
A.Process_exam_data()
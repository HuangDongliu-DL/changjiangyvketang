#coding=utf-8
'''
author:HuangDongliu
start time:12/18/2020
finall time:
function:长江雨课堂题目导出
'''
import requests
from time import sleep
import cv2
import pandas as pd
from cnocr import CnOcr
import numpy as np

class Rain_Classroom:
    '''
    长江雨课堂题目导出
    '''
    def __init__(self,classroom_id:int,quiz_id:int,start_problem_id:int,finally_problem_id:int,session_id:str,name:str):
        '''
        :param
            classroom_id int 班级编号
            quiz_id int 测试题编号
            session string tooken
            start_problem_id  int 开始序号
            finally_problem_id int 结束序号
        '''
        self.classroom_id = classroom_id
        self.quiz_id = quiz_id
        self.start_problem_id = start_problem_id
        self.finally_problem_id = finally_problem_id
        self.BASE_URL = "https://changjiang.yuketang.cn/v2/api/web/quiz/problem_shape"
        self.cookies = {
            "sessionid":session_id,
        }
        self.name = name
        self.HEADERS = {
                            'Connection': 'keep-alive',
                            'Pragma': 'no-cache',
                            'Cache-Control': 'no-cache',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
                            'Sec-Fetch-Dest': 'image',
                            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                            'Sec-Fetch-Site': 'same-site',
                            'Sec-Fetch-Mode': 'no-cors',
                            'Referer': 'https://www.yuketang.cn/v2/web/quizSummary/3545590/878580',
                            'Accept-Language': 'zh-CN,zh;q=0.9',
                        }
        # 创建Session
        self.session = requests.session()
        # 实例化OCR识别对象
        self.ocr = CnOcr()
    def alpha2white_opencv2(self,img:np.ndarray) -> np.ndarray:
        sp = img.shape
        width = sp[0]
        height = sp[1]
        for yh in range(height):
            for xw in range(width):
                color_d = img[xw, yh]
                # 找到alpha通道不為255的像素
                if (color_d[3] != 255):
                    # 改變這個像素
                    img[xw, yh] = [255, 255, 255, 255]
        return img
    def img2string(self,img:np.ndarray) -> str:
        img = self.alpha2white_opencv2(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        Str = ''
        res = self.ocr.ocr(img)
        for i in res:
            Str += ''.join(i)
        return Str
    def Get_image(self):
        Data = []
        for problem_id in range(self.start_problem_id,self.finally_problem_id+1):
            try:
                PARAMS = {
                    "classroom_id":self.classroom_id,
                    "quiz_id":self.quiz_id,
                    "problem_id":problem_id
                }
                r = self.session.get(self.BASE_URL,params=PARAMS,headers=self.HEADERS,cookies = self.cookies)
                Answer = r.json()['data']['Answer']
                Data_LIST = ["%s"%str(problem_id-self.start_problem_id + 1),"%s"%Answer]
                for i in r.json()['data']['Shapes']:
                    b = self.session.get(i['URL']).content
                    img = cv2.imdecode(np.frombuffer(b,np.uint8),cv2.IMREAD_UNCHANGED)
                    Data_LIST.append(self.img2string(img))
                print("%d 完成"%problem_id)
                sleep(0.5)
                Data.append(Data_LIST)
            except:
                pass
        pd.DataFrame(Data).to_csv(self.name+".CSV",encoding='GBK',index=False,index_label=False)
            
rain_classroom = Rain_Classroom(
    classroom_id=3979434,
    quiz_id=795573,
    start_problem_id=17659780,
    finally_problem_id=17660029,
    session_id = "1oqp0yrqfcjzeo3lnggkvaw7rr120gzn",
    name = "第四章(Ⅰ)"
)
rain_classroom.Get_image()

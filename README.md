# 长江雨课堂作业导出及考试自动答题

这个项目是由于马原期末考试要考平时再雨课堂里发布的试题，并且是再雨课堂上面进行机考。如果我们可以将平时的题目提取出来，做成一个题库然后在机考的时候程序自动抓取考试题并且与题库中的题目进行对比，然后提交。说干就干，于是就有了这个项目。



## 一、题目的提取

因为之前所发布的题目是用的长江雨课堂的旧版试卷形式，是通过ppt上传的，抓取下来全是图片所以需要通过中文OCR来识别一下，先是用的GOOGLE的tesserocr发现识别率太低了，后转用GITHUB上面的一个开源的中文OCR项目[cnocr](https://github.com/breezedeus/cnocr)，发现识别率挺高的。然后识别的数据就放在CSV文件中，后方便到时候程序匹配题目就将CSV文件中的数据全部合并到Sqlite3数据库中了。啰啰嗦嗦讲了这么多来了解一下如何使用吧

#### 1.开始使用

需要通过浏览器抓包得到，classroom_id(班级编号)，quiz_id（测试题编号），start_problem_id（开始题目编号），finally_problem（最后题目编号），session_id（用于构建cookie），name（到时候保存数据的名称）

```python
# Question_extraction.py
rain_classroom = Rain_Classroom(
    classroom_id=3979434,
    quiz_id=795573,
    start_problem_id=17659780,
    finally_problem_id=17660029,
    session_id = "1oqp0yrqfcjzeo3lnggkvaw7rr120gzn",
    name = "第四章(Ⅰ)"
)
rain_classroom.Get_image()
```

#### 2.技术笔记

- 直接将二进制数据转化为np.ndarry（Opencv图片格式）

  ```Python
  img = cv2.imdecode(np.frombuffer(b,np.uint8),cv2.IMREAD_UNCHANGED)
  ```

- 将透明图片转化为黑白图片

  ```python
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
  ```



## 二、自动答题脚本的构建


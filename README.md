# �����������ҵ�����������Զ�����

�����Ŀ��������ԭ��ĩ����Ҫ��ƽʱ��������﷢�������⣬�������������������л�����������ǿ��Խ�ƽʱ����Ŀ��ȡ����������һ�����Ȼ���ڻ�����ʱ������Զ�ץȡ�����Ⲣ��������е���Ŀ���жԱȣ�Ȼ���ύ��˵�ɾ͸ɣ����Ǿ����������Ŀ��



## һ����Ŀ����ȡ

��Ϊ֮ǰ����������Ŀ���õĳ�������õľɰ��Ծ���ʽ����ͨ��ppt�ϴ��ģ�ץȡ����ȫ��ͼƬ������Ҫͨ������OCR��ʶ��һ�£������õ�GOOGLE��tesserocr����ʶ����̫���ˣ���ת��GITHUB�����һ����Դ������OCR��Ŀ[cnocr](https://github.com/breezedeus/cnocr)������ʶ����ͦ�ߵġ�Ȼ��ʶ������ݾͷ���CSV�ļ��У��󷽱㵽ʱ�����ƥ����Ŀ�ͽ�CSV�ļ��е�����ȫ���ϲ���Sqlite3���ݿ����ˡ��������½�����ô�����˽�һ�����ʹ�ð�

#### 1.��ʼʹ��

��Ҫͨ�������ץ���õ���classroom_id(�༶���)��quiz_id���������ţ���start_problem_id����ʼ��Ŀ��ţ���finally_problem�������Ŀ��ţ���session_id�����ڹ���cookie����name����ʱ�򱣴����ݵ����ƣ�

```python
# Question_extraction.py
rain_classroom = Rain_Classroom(
    classroom_id=3979434,
    quiz_id=795573,
    start_problem_id=17659780,
    finally_problem_id=17660029,
    session_id = "1oqp0yrqfcjzeo3lnggkvaw7rr120gzn",
    name = "������(��)"
)
rain_classroom.Get_image()
```

#### 2.�����ʼ�

- ֱ�ӽ�����������ת��Ϊnp.ndarry��OpencvͼƬ��ʽ��

  ```Python
  img = cv2.imdecode(np.frombuffer(b,np.uint8),cv2.IMREAD_UNCHANGED)
  ```

- ��͸��ͼƬת��Ϊ�ڰ�ͼƬ

  ```python
      def alpha2white_opencv2(self,img:np.ndarray) -> np.ndarray:
          sp = img.shape
          width = sp[0]
          height = sp[1]
          for yh in range(height):
              for xw in range(width):
                  color_d = img[xw, yh]
                  # �ҵ�alphaͨ������255������
                  if (color_d[3] != 255):
                      # ��׃�@������
                      img[xw, yh] = [255, 255, 255, 255]
  ```



## �����Զ�����ű��Ĺ���


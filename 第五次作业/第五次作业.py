# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:43:43 2021

@author: qinqiushi
"""

import pandas as pd
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

a = []
d = pd.read_csv("Market_Basket_Optimisation.csv", header=None)
dic = {}

# 用字典来记录数据
for i in range(d.shape[0]):
    temp = []
    for j in range(d.shape[1]):
        b = str(d.values[i, j])
        if b != "nan":#略过空值
            temp.append(b)
            if b not in dic:
                dic[b] = 1
            else:
                dic[b] += 1
    a.append(temp)
ciku = ' '.join('%s' %b for b in a)

#排除停用词
stop_words = []
for s in stop_words:
    ciku = ciku.replace(s, '')

#分词
cut_text = word_tokenize(ciku)
cut_text = " ".join(cut_text)

#设置词云函数
wc = WordCloud(max_words=100, width=2000, height=1200)

#生成词云图片
ciyun = wc.generate(cut_text)
ciyun.to_file('词云.jpg')
wordcloudpicture = plt.imread('词云.jpg')
plt.imshow(wordcloudpicture)
plt.axis("off")
plt.show()

#显示前十商品
print("前十商品:")
print(sorted(dic.items(),key=lambda x:x[1],reverse=True)[:10])



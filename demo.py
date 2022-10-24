#-*-coding:utf-8-*-
'''
File Name:demo.py
Create File Time:2022/10/17 22:27
Author:Leemc-GAO
'''
import wordcloud as wc
import matplotlib.pyplot as plt
import jieba
from PIL import Image
from numpy import array
from jieba.analyse import extract_tags
import numpy as np
from numpy import arange
import matplotlib

path="E:\Desktop\二十大\ershida.txt"
data=open(path,"r",encoding="UTF-8").read()
cutdata=jieba.cut(data)
jieba.setLogLevel(jieba.logging.INFO)
alldata=""
for i in cutdata:
    alldata=alldata+" "+str(i)
pic=Image.open("E:\Desktop\二十大\dang.jpg")
picarry=array(pic)
font = r'C:\Windows\Fonts\方正粗黑宋简体.ttf'
mywc=wc.WordCloud(collocations=False,font_path=font,mask=picarry,background_color="white").generate(alldata)
fig=plt.figure(figsize=(10,10))
plt.imshow(mywc)
plt.axis("off")
plt.show()

tags = extract_tags(sentence=alldata, topK=20)

words = [word for word in jieba.cut(data, cut_all=True)]
words_freq = {}
for tag in tags:
    freq = words.count(tag)
    words_freq[tag] = freq

usedata=sorted(words_freq.items(), key=lambda d:d[1])

tmp= np.array(usedata).T
print(tmp)

fig,ax = plt.subplots(figsize=(10,10))

myfont = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\方正粗黑宋简体.ttf")

plt.title(u'       二十大大报告词频统计',fontproperties=myfont,fontsize=20,x=0.001,y=1.02)
ax.set_xlabel(u'出现次数',fontproperties=myfont,fontsize=20,x=0.06,y=1.02,color="gray")

ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')

tick_positions = range(1,21)
ax.set_yticks(tick_positions)
ax.set_yticklabels(tmp[0],fontproperties=myfont,fontsize=18,color="gray")

bar_positions = arange(20) + 0.75

ax.barh(bar_positions, tmp[1], 0.5,align="edge")
plt.show()
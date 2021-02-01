import numpy
from numpy import *

subject={'Chinese': '语文', 'math': '数学', 'English': '英语'}
t=dtype([('name', str, 40), ('Chinese', int32), ('math', int32), ('English', int32)])
score=array([('张飞', 68, 65, 30), ('关羽', 95, 76, 98), ('刘备', 98, 86, 88), ('典韦', 90, 88, 77), ('许褚', 80, 90, 90)], dtype=t)
total_score={}
a=1

for i in subject:
	print("%s科目的平均成绩为：%.2f，最小成绩为%d，最大成绩为%d，方差为%f，标准差为%f。" %(subject[i], mean(score[i]), min(score[i]), max(score[i]), var(score[i]), std(score[i])))

for m in score:
	sum=0
	for n in range(1, 4):
		b=int(m[n])
		sum=sum+b
	total_score[m[0]]=sum
rank=sorted(total_score.items(), key=lambda x: x[1], reverse=True)
print('\n')
print('总成绩排名依次为：', end='')
for j in rank:
	print('第%d名：%s' %(a, j[0]), end='  ')
	a += 1
print('\n')
input('按回车键结束程序')
	
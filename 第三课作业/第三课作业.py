# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

#读取csv文件
data = pd.read_csv(r'C:\Users\admin\OneDrive\python作业\第三课作业\car_data.csv', encoding='gbk')
train_x = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]

# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)
print(train_x)


#使用KMeans聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("分类结果.csv",index=False)
input('按回车键结束')
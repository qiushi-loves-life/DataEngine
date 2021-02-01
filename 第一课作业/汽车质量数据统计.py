import pandas
from pandas import * 

#读入文件
df = read_csv( r'C:\Users\QinQiushi\OneDrive\python作业\第一课作业\car_complain.csv')
df.head

#预处理
df['brand']=df['brand'].replace('一汽大众','一汽-大众')

#统计每个品牌的投诉总量
brand_count=df.groupby(['brand'])['id'].agg(['count'])
brand_count=brand_count.rename(columns={'count':'brandComplain_count'})

#统计每个车型的投诉总量
carModel_count=df.groupby(['car_model'])['id'].agg(['count'])
carModel_count=carModel_count.rename(columns={'count':'carModelComplain_count'})

#统计每个品牌各有多少车型被投诉
df1=df.drop_duplicates(['car_model'])
brand_carModel=df1.groupby(['brand'])['car_model'].agg(['count'])
brand_carModel=brand_carModel.rename(columns={'count':'car_count'})

#统计每个品牌的平均车型投诉量（品牌的投诉总数除以该品牌收到投诉的车型数量）
df2 = merge(brand_count, brand_carModel, how='outer', on='brand')
df2['average_complain']=df2['brandComplain_count']/df2['car_count']

#输出结果
df2.sort_values(by='average_complain', ascending=False, inplace=True)
print(df2)
print('每个品牌的平均车型投诉量最高的是：%s' %(df2.index[0]))


input('按回车键结束程序')


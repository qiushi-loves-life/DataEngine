import pandas as pd
from efficient_apriori import apriori
tran = [] #交易

d = pd.read_csv('Market_Basket_Optimisation.csv', header = None)#读取文件中的数据
for a in range(0, d.shape[0]):
    temp = []
    for b in range(0, 20):
        if str(d.values[a, b]) != 'nan':
            temp.append(str(d.values[a, b]))
    tran.append(temp)

#频繁项集和频繁规则
print(tran, '\n')
pinfanxiangji, guanlianguize = apriori(tran, min_support = 0.02,  min_confidence = 0.4)
print('频繁项集：', pinfanxiangji, '\n')
print('关联规则：', guanlianguize)
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

#读取数据
df = pd.read_csv('./train.csv')

#按时间索引
df.Datetime = pd.to_datetime(df.Datetime, format='%d-%m-%Y %H:%M')
df.index = df.Datetime
df1 = df.resample('D').sum()
df_day = df1.reset_index()
df_day.rename(columns={'Datetime':'ds', 'Count':'y'}, inplace=True)

# 拟合
model = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.05)
model.fit(df_day)

# 预测接下来7个月的数据（30*7=210）
future = model.make_future_dataframe(periods=210)
forecast = model.predict(future)

# 生成预测结果图片并展示
model.plot(forecast)
plt.savefig('预测结果.jpg')
plt.show()
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
series = pd.Series([1, 3, 4, 6, 8])
print(series)
# %%
series = pd.Series([1, 3, 4, np.nan, 6, 8])
print(series)
# %%
name = pd.Series(['김수안', '김수정', '박동윤', '간이안', '강지안'])
grade = pd.Series([4.35, 4.23, 4.25, 4.37, 4.25])
sex = pd.Series(['F', 'F', 'M', 'F', 'M'])
age = pd.Series([19, 23, 22, 19, 16])
df = pd.DataFrame({'name': name, 'grade': grade, 'age': age, 'sex': sex})
print(df)
# %%
df = pd.read_csv('dataset/countries.csv', index_col=0)
print(df)

df_no_idx = pd.read_csv('dataset/countries.csv')
print(df_no_idx)
# %%
print(df[['area', 'population']])
# %%
countries = df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))
plt.show()
countries = df['population'].plot(kind='pie', color=('b', 'darkorange', 'g', 'r', 'm'))
plt.show()
# %%
weather = pd.read_csv('dataset/weather.csv', index_col=0, encoding='utf-8')
weather = weather['평균풍속'].plot(kind='hist', bins=33)
plt.show()
# %%
print(df.head())
print(df[:3])
# %%
print(df.loc['KR'])
print(df['population'][:3])
print(df.loc['US', 'capital'])
print(df['capital'].loc['US'])
# %%
df['density'] = df['population'] / df['area']
print(df)
# %%
weather = pd.read_csv('dataset/weather.csv', index_col=0, encoding='utf-8')
print(weather.describe())
# %%
print('평균')
print(weather.mean())
print('표준편차')
print(weather.std())
# %%
print(weather.count())
print(weather['최대풍속'].count())
# %%
print(weather[['최대풍속', '평균풍속']].count())
print(weather[['최대풍속', '평균풍속']].mean())
print(weather.mean()[['최대풍속', '평균풍속']])
# %%
weather = pd.read_csv('dataset/weather.csv', index_col=0, encoding='utf-8')
monthly = [None for x in range(12)]
monthly_wind = [0 for x in range(12)]

weather['month'] = pd.DatetimeIndex(weather['일시']).month

for i in range(12):
    monthly[i] = weather[weather['month'].dt.month == i+1]
    monthly_wind[i] = monthly[i]['평균풍속'].mean()

plt.plot(monthly_wind, 'red')
plt.show()
# %%
weather['최대풍속'] >= 10.0
# %%
weather[weather['최대풍속'] >= 10.0]
# %%
weather['평균풍속'].isna()
# %%
missing_data = weather[weather['평균풍속'].isna()]
print(missing_data)
# %%
weather.dropna(axis=0, how='any', inplace=True)
weather.fillna(0, inplace=True)
print(weather.loc['2012-02-11'])
# %%

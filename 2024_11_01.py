# %%
import os
import pandas as pd

# %%
os.makedirs('dataset', exist_ok=True)

index = [2015, 2016, 2017, 2018, 2019, 2020]
data = {
    '1분기': [500, 690, 1100, 1500, 1990, 1020],
    '2분기': [450, 700, 1030, 1650, 2020, 1600],
    '3분기': [520, 820, 1200, 1700, 2300, 2200],
    '4분기': [610, 900, 1380, 1850, 2420, 2550]
}
df = pd.DataFrame(data, index=index)

df.to_csv('dataset/pandas3.csv', mode='w', encoding='utf-8')

csv = pd.read_csv('dataset/pandas3.csv', encoding='utf-8')
print(csv.info())
# %%
import matplotlib.pyplot as plt

df = pd.DataFrame({
    '지점': ['a', 'a', 'b', 'b'],
    '상품': ['p1', 'p2', 'p1', 'p2'],
    'q1': [112, 134, 156, 178],
    'q2': [212, 234, 256, 278],
    'q3': [312, 334, 356, 378],
    'q4': [412, 434, 456, 478],
})
df['q1'].plot()
plt.show()
# %%
ser1 = pd.Series([300, 100, 200, 500])
ser1.plot()
plt.show()
# %%
ser2 = pd.Series([300, 100, 200, 500], index=[2, 1, 0, 4])
ser2.plot()
plt.show()
# %%
ser2.sort_index().plot()
plt.show()
# %%
ser1.plot.line(color='#ff0000', lw=5, title='linear_graph')
plt.show()
# %%
df['q1'].plot(kind='bar')
plt.show()
# %%
df['q1'].plot(kind='bar', color='#ff0000')
plt.show()
# %%
df['q1'].plot.bar(
    color='#ff0000',
    edgecolor='#000000',
    linewidth=3,
    title='title',
    xlabel='x-axis',
    ylabel='y-axis',
)
plt.show()
# %%
df['q1'].plot(kind='pie')
plt.show()
# %%
df['q1'].plot(kind='pie', autopct='%1.1f%%')
plt.show()
# %%

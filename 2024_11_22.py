# %%
import pandas as pd

# %%
red_df = pd.read_csv('dataset/winequality-red.csv', sep=';', header=0, engine='python')
white_df = pd.read_csv('dataset/winequality-white.csv', sep=';', header=0, engine='python')

# %%
red_df.to_csv('dataset/winequality-red.csv', sep=',', index=False)
white_df.to_csv('dataset/winequality-white.csv', sep=',', index=False)

# %%
print(red_df.head())
print(white_df.head())

# %%
df = pd.concat([red_df, white_df])
df.to_csv('dataset/integrated_winequality.csv', sep=',', index=False)

# %%
print(df.head())
print(df.info())

# %%
df.columns = df.columns.str.replace(' ', '_')

# %%
print(df.head())
print(df.describe())

# %%
# 추가된 내용
df = pd.read_csv('dataset/integrated_winequality.csv', header=None)
df = df[0].str.split(',', expand=True)
df.columns = df.iloc[0]
df = df[1:]
df.to_csv('dataset/integrated_winequality.csv', index=False)

# %%
sorted(df['quality'].unique())
print(df['quality'].value_counts())

# %%
# print(df.groupby('type')['quality'].describe())
# print(df.groupby('type')['quality'].mean())
# print(df.groupby('type')['quality'].std())
# print(df.groupby('type')['quality'].agg('mean', 'std'))

# %%

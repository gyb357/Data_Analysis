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
df.to_csv('dataset/winequality.csv', sep=',', index=False)

# %%
print(df.head())
print(df.info())

# %%
df.columns = df.columns.str.replace(' ', '_')
df.to_csv('winequality.csv', index=False)

# %%
print(df.describe())

# %%
print(sorted(df.quality.unique()))
print(df.quality.value_counts())

# %%

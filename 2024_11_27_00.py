# %%
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# %%
# %pip install scipy
# %pip install statsmodels
# %pip install seaborn

# %%
red_df = pd.read_csv('dataset/winequality-red.csv', sep=';', header=0, engine='python')
white_df = pd.read_csv('dataset/winequality-white.csv', sep=';', header=0, engine='python')
red_df.columns = red_df.columns.astype('str')
red_df.columns = red_df.columns.str.replace('"', '')

print(red_df.head())
print(white_df.head())

# %%
# red_df.to_csv('dataset/winequality-red.csv', sep=',', index=False)
# white_df.to_csv('dataset/winequality-white.csv', sep=',', index=False)
# 스페이스 바가 포함된 컬럼명을 언더바로 변경
red_df.columns = red_df.columns.str.replace(' ', '_')
white_df.columns = white_df.columns.str.replace(' ', '_')

# %%
red_df.insert(0, column='type', value='red')
white_df.insert(0, column='type', value='white')

# %%
print(red_df.head())
print(white_df.head())

# %%
df = pd.concat([red_df, white_df])
df.to_csv('dataset/winequality.csv', sep=',', index=False)
# -------------------------------------------------- #

# %%
df = pd.read_csv('dataset/winequality.csv', sep=',', header=0, engine='python')

# %%
print(df.head())
print(df.info())

# %%
sorted(df['quality'].unique())
print(df['quality'].value_counts())

# %%
print(df.groupby('type')['quality'].describe())
print(df.groupby('type')['quality'].mean())
print(df.groupby('type')['quality'].std())
print(df.groupby('type')['quality'].agg('mean', 'std'))

# %%
group1 = [1, 2, 3, 4, 5]
group2 = [3, 4, 5, 6, 7]

t_statistic, p_value = stats.ttest_ind(group1, group2)
print('t_statistic:', t_statistic)
print('p_value:', p_value)

# %%
mean1 = 10
mean2 = 12
std1 = 3
std2 = 4
n1 = 20
n2 = 30

t, p = stats.ttest_ind_from_stats(mean1, std1, n1, mean2, std2, n2)
print('t_statistic:', t)
if p < 0.05:
    print('p_value:', p, 'Reject the null hypothesis')
else:
    print('p_value:', p, 'Accept the null hypothesis')

# %%
red_df_quality = df.loc[df['type'] == 'red', 'quality']
white_df_quality = df.loc[df['type'] == 'white', 'quality']
stats.ttest_ind(red_df_quality, white_df_quality, equal_var=False)

r_formula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
lm = ols(r_formula, df).fit()
print(lm.summary())

# %%
sample1 = df[df.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
sample1_predict = lm.predict(sample1)
print(sample1_predict)

# %%
print(df[0:5][:])

# %%
data = {
    'fixed_acidity': [8.5, 8.1],
    'volatile_acidity': [0.8, 0.5],
    'citric_acid': [0.3, 0.4],
    'residual_sugar': [6.1, 5.8],
    'chlorides': [0.055, 0.04],
    'free_sulfur_dioxide': [30.0, 31.0],
    'total_sulfur_dioxide': [98.0, 99.0],
    'density': [0.996, 0.91],
    'pH': [3.25, 3.01],
    'sulphates': [0.4, 0.35],
    'alcohol': [9.0, 0.88]
}
sample2 = pd.DataFrame(data, columns=sample1.columns)
print(sample2)

# %%
sample2_predict = lm.predict(sample2)
print(sample2_predict)

# %%
sns.set_style('dark')
sns.histplot(red_df_quality, stat='density', kde=True, color='red', label='Red Wine')
sns.histplot(white_df_quality, stat='density', kde=True, color='blue', label='White Wine')
plt.title('Quality of Wine Type')
plt.legend()
plt.show()

# %%
others = list(set(df.columns).difference(set(['quality', 'fixed_acidity'])))
p, resids = sm.graphics.plot_partregress('quality', 'fixed_acidity', others, data=df, obs_labels=False)
plt.show()

# %%3
fig = plt.figure(figsize=(8, 13))
sm.graphics.plot_partregress_grid(lm, fig=fig)
plt.show()

# %%

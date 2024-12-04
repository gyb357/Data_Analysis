# %%
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = sns.load_dataset('titanic')
df.to_csv('dataset/titanic.csv', index=False)

# %%
print(df.isnull().sum())

# %%
df['age'] = df['age'].fillna(df['age'].median())

print(df['embarked'].value_counts())
df['embarked'] = df['embarked'].fillna('S')

# %%
print(df['embark_town'].value_counts())
df['embark_town'] = df['embark_town'].fillna('Southampton')

# %%
print(df['deck'].value_counts())
df['deck'] = df['deck'].fillna('C')

# %%
print(df.isnull().sum())

# %%
print(df.info())

# %%
print(df.survived.value_counts())

# %%
f, ax = plt.subplots(1, 2, figsize=(10, 5))
df['survived'][df['sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
df['survived'][df['sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
ax[0].set_title('Survived (male)')
ax[1].set_title('Survived (female)')
plt.show()

# %%
sns.countplot(x='pclass', hue='survived', data=df)
plt.title('Pclass: Survived vs Dead')
plt.show()

# %%
df2 = df.select_dtypes(include=[int, float, bool])
print(df.shape)

df_corr = df2.corr(method='pearson')
print(df_corr)

# %%
df_corr.to_csv('dataset/titanic_corr.csv', index=False)

# %%
print(df['survived'].corr(df['adult_male']))
print(df['survived'].corr(df['fare']))

# %%
sns.pairplot(df, hue='survived')
plt.show()

# %%
sns.catplot(x='pclass', y='fare', hue='survived', kind='swarm', data=df)
plt.show()

# %%
def category_age(x):
    if x < 10:
        return 0
    elif x < 20:
        return 1
    elif x < 30:
        return 2
    elif x < 40:
        return 3
    elif x < 50:
        return 4
    elif x < 60:
        return 5
    elif x < 70:
        return 6
    else:    
        return 7
    
df['age2'] = df['age'].apply(category_age)
df['sex'] = df['sex'].map({'male': 1, 'female': 0})
df['family'] = df['sibsp'] + df['parch'] + 1
df.to_csv('dataset/titanic2.csv', index=False)

# %%
heatmap_data = df[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]
color_map = plt.cm.RdBu
sns.heatmap(heatmap_data.astype(float).corr(), linewidths=0.1, vmax=1.0, square=True, cmap=color_map, linecolor='white', annot=True, annot_kws={'size': 10})
plt.show()

# %%

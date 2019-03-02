# sympy library
import sympy

x, y = sympy.symbols('x y')
sympy.expand((x + y) ** 10)

from sympy import init_printing

init_printing(use_latex='maathjax')
sympy.solve(x ** 2 + 5 * x - y, x)
sympy.sin(x).series(n=15)
sympy.sin(x ** 2).series(n=15)
sympy.Matrix([[1, 2], [x, 1]]).det()

# pandas library
import pandas as pd

ser = pd.Series([2, 6, 12, 5])
print(ser)
print(ser[2])

algebra = pd.Series([4, 5, 3], index=['Alice', 'Bob', 'Claudia'])
print(algebra)
print(algebra['Alice'])
print(algebra['Bob'])
print(algebra[0])

calculus = pd.Series([5, 2, 5], index=['Alice', 'Bill', 'Claudia'])
print(calculus)
print(calculus + algebra)
print((calculus + algebra).sort_values())
print((calculus + algebra).sort_index(ascending=False))

ser = pd.Series([0, 10, 20, 30], index=[2, 3, 4, 10])
print(ser)
print(ser[3])
print(ser.iloc[3])
print(ser[2:4])
print(ser.loc[2])
print(ser.loc[3])
print(ser.loc[2:4])

print(calculus['Alice':'Bill'])

# table in pandas
df = pd.DataFrame([[3, 4, 5], [5, 2, 3]])
print(df)
df = pd.DataFrame([[3, 4, 5], [5, 2, 3], [5, 2, 1]],
                  index=['Alice', 'Bob', 'Claudia'],
                  columns=['Algebra', 'Calculus', 'Macro'])
print(df)
print(df['Algebra'])
print(df.loc['Alice'])
print(df.loc['Alice':'Bob'])
print(df.loc['Alice', 'Algebra'])
print(df.loc[:, 'Algebra':'Calculus'])
print(df.iloc[0])
print(df.iloc[0, 0])
print(df.iloc[:, 0])
print(df[['Algebra', 'Macro']])
print(df.loc[:, ['Algebra', 'Macro']])
print(df.mean(axis=0))
print(df.mean(axis=1))
print(df.max(axis=0))
print(df[df['Algebra'] > 3])
print(df.Algebra)
df['Micro'] = [4, 2, 5]
print(df)
df['Micro'] = pd.Series([2, 5, 3], index=['Bob', 'Claudia', 'Alice'])
print(df)
df.loc['Julia'] = [5, 5, 5, 5]
print(df)
df['last_name'] = ['Smith', 'Smith', 'Ivanova', 'Petrova']
print(df)
print(df.dtypes)
print(df.last_name.str.endswith('va'))

df = pd.read_csv("https://bit.ly/2A2zkI6")
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())
print(df.tail())
print(df[:3])
print(df.color.value_counts())
print(df.color.unique())
df['color'] = df['color'].str.strip()
print(df.color.value_counts())
print(df.color.value_counts(dropna=False))
print(df.groupby('country').mean())
print(df.groupby('country')['imdb_score'].mean())
print(df.groupby('country')['imdb_score'].mean().sort_values(ascending=False))
print(df['title_year'].min())
print(df['title_year'].max())
print(df[df['country'] == 'Kyrgyzstan'][['title_year', 'movie_title']])
print(df.query('country == "Kyrgyzstan"'))
print(df.query('country == "USA" and color == "Black and White"')['title_year'].max())
df.rename(columns={'title_year': 'year'}, inplace=True)
print(df.columns)
df.drop('director_name', axis=1, inplace=True)
print(df.loc[df.duration.idxmax(), 'movie_title'])

import matplotlib.pyplot as plt

df.query('imdb_score > 8').groupby('year')['duration'].mean().plot()
plt.tight_layout()
plt.savefig("years.pdf")

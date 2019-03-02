import pandas as pd

students = pd.DataFrame([['Alice', 973243],
                         ['Bob', 123121],
                         ['Claudia', 7651231]], columns=['student', 'id'])

gradebook = pd.DataFrame([[123121, 5, 4],
                          [7651231, 4, 3],
                          [7654599, 3, 3]], columns=['id_number', 'Algebra', 'Calculus'])

print(students)
print(gradebook)

inner_join_df = students.merge(gradebook, left_on='id', right_on='id_number')
print(inner_join_df)

left_join_df = students.merge(gradebook, how='left', left_on='id', right_on='id_number')
print(left_join_df)

outer_join_df = students.merge(gradebook, how='outer', left_on='id', right_on='id_number')
print(outer_join_df)

# Check fo NaN
import numpy as np

x = np.nan
print(x)
print(x == np.nan)
print(x == float("NaN"))
print(float("inf") == float("inf"))
print(np.isnan(x))
print(np.isnan(float("NaN")))

# Replace NaN
print(outer_join_df.isnull().any(axis=1))
print(outer_join_df.dropna())
print(outer_join_df.dropna(subset=['student']).fillna(0))

journal = pd.DataFrame([['Alice', 'Algebra', 5],
                        ['Bon', 'Calculus', 3],
                        ['Alice', 'Calculus', 4]], columns=['student', 'course', 'grade'])
print(journal)
table = journal.pivot(index='student', columns='course', values='grade')
print(table)
print(outer_join_df.dropna().melt(id_vars='student',
                                  value_vars=['Algebra', 'Calculus'],
                                  var_name='course',
                                  value_name='grade'))

journal = pd.DataFrame([['Alice', 'Algebra', 5],
                        ['Bon', 'Calculus', 3],
                        ['Alice', 'Calculus', 4],
                        ['Alice', 'Calculus', 5]], columns=['student', 'course', 'grade'])
print(journal.pivot_table(index='student', columns='course', values='grade'))
print(journal.pivot_table(index='student', columns='course', values='grade', aggfunc='last'))

url = "http://math-info.hse.ru/f/2014-15/nes-stat/climate.html"
tables = pd.read_html(url, header=0)
print(type(tables))
print(len(tables))
df = tables[0]
print(df)
print(df.dtypes)
print(df.head())
df_prep = df.dropna().drop(['STATION_ID', 'STATION_NM', 'Q', 'Q.1', 'Q.2', 'D'], axis=1)
print(df_prep)
print(df_prep[:365])
print(df_prep[:3650].drop('DATE_OBS', axis=1).rolling(window=30).mean())
df_prep.index = pd.to_datetime(df_prep['DATE_OBS'])
print(df_prep)
print(df_prep["1949-01"])
print(df_prep.drop('DATE_OBS', axis=1).rolling(window=365 * 10).mean())
print(df_prep.index.year)
df_prep['year'] = df_prep.index.year
df_prep['month'] = df_prep.index.month
df_prep['day'] = df_prep.index.day
print(df_prep)
corr = df_prep.pivot_table(index='year', columns='month', values='TMPMN').dropna().corr()
print(corr)

# web scraping
from IPython.display import HTML

html = """
<h1>Hello</h1>
<p>This is a paragraph with <a href="http;//hse.ru>link</a>.</p>"""
print(HTML(html))

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup)
print(soup.find("p"))
print(soup.find_all("p"))
print(soup.find("a")['href'])

import requests

r = requests.get("https://www.hse.ru/")
print(r)
print(r.text[:300])
soup = BeautifulSoup(r.text, 'lxml')
for h3 in soup.find_all("h3", class_="post__title"):
    print(h3.text.strip())

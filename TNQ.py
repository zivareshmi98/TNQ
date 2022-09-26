import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import re
pd.set_option('display.expand_frame_repr', False)
path=r"D:\TASK\Scenario_Based _Questions\List of the Countries and Territories.txt"
df=pd.read_csv(path)
# print(df)
path1=r"D:\TASK\Scenario_Based _Questions\world_population.csv"
df1=pd.read_csv(path1)
print(df1.head(5))
# print(df1)
##Finding the duplicate:
df2=df1.duplicated().sum()
# print(df2)
##Sum of world population percentage:
temp = df1.groupby('Continent').sum()['World Population Percentage']
# print(temp)

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
palette_color = sns.color_palette('magma')
ax.pie(x=temp.values, labels=temp.index, radius=2, autopct='%0.2f%%', shadow=True, explode=[0, 0.1, 0, 0, 0, 0], colors=palette_color)
plt.title(label='world population percentage',
          loc="left",
          fontstyle='italic')
ax.axis('equal')


circle = plt.Circle((0, 0),1,fc='black')
g = plt.gcf()
g.gca().add_artist(circle)
# plt.show()

################################################

regx=re.compile(r'\d{4} \w+')
temp = [i[0] for i in map(regx.findall, df1.columns) if len(i) != 0]

fig, ax = plt.subplots()
pd.pivot_table(data=df1, columns='Continent', values=df1[temp], aggfunc='sum').plot(kind='line', ax=ax, ylabel='In Billion')
plt.title(label='population growth on each continent',
         loc='left',
         fontstyle='italic',
         size=12)
plt.xticks(rotation=45)
ax.legend(bbox_to_anchor=(1,1))
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x)//10**9, ',')))
# plt.show()
#############################
fig, ax = plt.subplots(1, 2, figsize=(15,3))
palette_color = sns.color_palette('magma')
df1[['Country', 'Density (per km²)']].sort_values(by='Density (per km²)', ascending=False).iloc[:5, :].set_index('Country').plot(kind='bar',
                                                                                                                                   color=palette_color,
                                                                                                                                   legend=False,
                                                                                                                                   ax=ax[0],
                                                                                                                                   xlabel='',
                                                                                                                                   ylabel='Density Population',
                                                                                                                                   title='top 5 countries with the largest population density')
df1[['Country', 'Density (per km²)']].sort_values(by='Density (per km²)').iloc[:5, :].set_index('Country').plot(kind='bar',
                                                                                                                  color=palette_color,
                                                                                                                  legend=False,
                                                                                                                  ax=ax[1],
                                                                                                                  xlabel='',
                                                                                                                  ylabel='Density Population',
                                                                                                                  title='top 5 countries with the smallest population density')
ax[0].tick_params(labelrotation=45)
ax[1].tick_params(labelrotation=45)
# plt.show()
######################################
area = df1['Area (km²)'].sum()
area = (df1.groupby('Continent').sum()['Area (km²)'] / area * 100)

fig, ax = plt.subplots()
palette_color = sns.color_palette('magma')
plt.pie(x=area.values, labels=area.index, radius=2, autopct='%0.2f%%', shadow=True, explode=[0, 0.2, 0, 0, 0, 0], colors=palette_color)
plt.title(label='the area of each continent',
          loc="left",
          fontstyle='italic',
          size=12)
ax.axis('equal')
# plt.show()
###################################
palette_color = sns.color_palette('magma')
df1.groupby('Continent').count()['Country'].plot(kind='bar', color=palette_color, title='the number of countries on each continent', xlabel='')
plt.xticks(rotation=45)
# plt.show()
#################################
temp = df1.loc[df1['Country'] == 'Indonesia'][temp]

fig, ax = plt.subplots()
sns.lineplot(x=temp.columns[::-1], y=temp.values[0][::-1])
plt.xticks(rotation=45)
plt.title('population growth in indonesia')
plt.ylabel('in million')
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x)//10**6, ',')))
plt.show()
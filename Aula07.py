


import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Aracaju.xlsx')
df2 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Fortaleza.xlsx')
df3 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Natal.xlsx')
df4 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Recife.xlsx')
df5 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Salvador.xlsx')

df = pd.concat([df1,df2,df3,df4,df5])


df['LojaID'].value_counts(ascending=False).plot.bar() # gráfico na vertical

df['LojaID'].value_counts(ascending=True).plot.barh() # gráfico na Horizontal

df.groupby(df['Data'].dt.year)['Vendas'].sum().plot.pie() # Agrupando info. e exibindo em gráfico de Pizza

print(df['Cidade'].value_counts())


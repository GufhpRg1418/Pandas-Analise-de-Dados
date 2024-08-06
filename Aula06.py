

import pandas as pd

df1 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Aracaju.xlsx')
df2 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Fortaleza.xlsx')
df3 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Natal.xlsx')
df4 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Recife.xlsx')
df5 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Salvador.xlsx')

df = pd.concat([df1,df2,df3,df4,df5])

# df['Data'] = df['Data'].astype('int64')

# df['Data'] = df.to_datetime(df['Data'])

#print(df.groupby(df['Data'].dt.year)['Vendas'].sum())

# df['Ano Venda'] = df['Data'].dt.year

# df['Mes_venda'], df['dia_venda'] = (df['Data'].dt.month, df['Data'].dt.day)

# print(df['Data'].min())

# df['diferenca_dias'] = df['Data'] - df['Data'].min()

# df['Trimestre_venda'] = df['Data'].dt.quarter

vendas_marco = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]

# print(df.sample(vendas_marco))

print(vendas_marco.sample(20))
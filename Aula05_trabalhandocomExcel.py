


import pandas as pd

df1 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Aracaju.xlsx')
df2 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Fortaleza.xlsx')
df3 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Natal.xlsx')
df4 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Recife.xlsx')
df5 = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Salvador.xlsx')

df = pd.concat([df1,df2,df3,df4,df5])

print(df3.head())

df['LojaID'] = df['LojaID'].astype('object')
print(df.dtypes)


# print(df.isnull().sum())

# df['Vendas'].fillna(df['Vendas'].mean(), implace=True)

# print(df['Vendas'].mean())

# df['Vendas'].fillna(0, inplace=True)

# df.dropna(subset=['Vendas'], inplace=True)

# df.dropna(how='all', inplace=True)


# df['Receita'] = df['Vendas'].mul(df['Qtde'])

# df['Receita / Vendas'] = df['Receita'] / df['Vendas']

#print(df.groupby('Cidade')['Vendas'].sum())

print(df.sort_values('Vendas', ascending=False).head(10))


# print(df.head())
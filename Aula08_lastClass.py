

import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo Excel
df = pd.read_excel('C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\AdventureWorks.xlsx')

# Verificar as primeiras linhas do DataFrame e suas dimensões
# print(df.head())
# print(df.shape)
# print(df.dtypes)

# Calcular o valor total de vendas
# print(df['Valor Venda'].sum())

# Calcular o custo total
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])
round(df['Custo'].sum(), 2)

# Calcular o lucro
df['lucro'] = df['Valor Venda'] - df['Custo']
round(df['lucro'].sum(), 2)

# Garantir que as colunas de data estão no formato datetime
df['Data Venda'] = pd.to_datetime(df['Data Venda'])
df['Data Envio'] = pd.to_datetime(df['Data Envio'])

# Calcular o tempo de envio em dias
df['Tempo_envio'] = (df['Data Envio'] - df['Data Venda']).dt.days

#Agrupar por marca e calcular o tempo médio de envio
print(df.groupby('Marca')['Tempo_envio'].mean())

#Verificar valores nulos
print(df.isnull().sum())

#Agrupar por ano de venda e marca, e calcular o lucro total
print(df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum())

# Configurar a exibição de floats
pd.options.display.float_format = '{:20,.2f}'.format

# Criar um DataFrame com o lucro anual por marca
lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum().reset_index()

produto = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True)

df_2009 = df[df['Data Venda'].dt.year == 2009]

print(df_2009)
# print(df.sample(10))



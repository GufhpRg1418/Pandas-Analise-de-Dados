
# Importa a biblioteca pandas e a renomeia como pd
import pandas as pd

# Define o caminho do arquivo CSV
file_path = 'C:\\Users\\gustavo.figueredo\\Desktop\\Developers Python Dio\\Analise de Dados com Python e Pandas\\Gapminder.csv'

# Lê o arquivo CSV especificado e o armazena em um DataFrame, especificando que o separador é ponto e vírgula (;)
df = pd.read_csv(file_path, sep=";")

# Renomeia as colunas do DataFrame
df = df.rename(columns={
    'country': 'Pais',          # 'country' para 'Pais'
    'continent': 'Continente',  # 'continent' para 'Continente'
    'year': 'Ano',              # 'year' para 'Ano'
    'lifeExp': 'Exp_vida',      # 'lifeExp' para 'Exp_vida'
    'pop': 'Pop Total',         # 'pop' para 'Pop Total'
    'gdpPercap': 'PIP'          # 'gdpPercap' para 'PIP'
})

# Imprime as primeiras 10 linhas do DataFrame para verificação
print(df.head(10))

# Imprime o número de linhas e colunas do DataFrame
print(df.shape)

# Imprime o nome das colunas do DataFrame
print(df.columns)

# Imprime os tipos de dados de cada coluna do DataFrame
print(df.dtypes)

# Imprime as últimas 15 linhas do DataFrame
print(df.tail(15))

# Imprime estatísticas descritivas do DataFrame
print(df.describe())

# Filtra o DataFrame para incluir apenas as linhas onde a coluna 'Continente' é 'Oceania'
Oceania = df.loc[df['Continente'] == 'Oceania']

# Imprime as primeiras linhas do DataFrame filtrado
print(Oceania.head())

# Imprime os valores únicos na coluna 'Continente' do DataFrame filtrado
print(Oceania['Continente'].unique())

# Imprime os valores únicos na coluna 'Continente' do DataFrame original
print(df['Continente'].unique())

# Agrupa o DataFrame pelo valor na coluna 'Continente' e conta o número de países únicos em cada grupo
print(df.groupby('Continente')['Pais'].nunique())

# Agrupa o DataFrame pelo valor na coluna 'Ano' e calcula a média da coluna 'Exp_vida' para cada ano
print(df.groupby('Ano')['Exp_vida'].mean())

# Calcula e imprime a média da coluna 'PIP'
print(df['PIP'].mean())

# Calcula e imprime a soma da coluna 'PIP'
print(df['PIP'].sum())

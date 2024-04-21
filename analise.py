import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_vendas.csv')

print("Primeiras linhas do DataFrame:")
print(df.head())
print()

print("Resumo estatístico das colunas numéricas:")
print(df.describe())
print()

plt.figure(figsize=(8, 5))
sns.countplot(x='Produto Vendido', data=df)
plt.title('Distribuição de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Número de Vendas')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Canal de Vendas', data=df)
plt.title('Distribuição de Vendas por Canal de Vendas')
plt.xlabel('Canal de Vendas')
plt.ylabel('Número de Vendas')
plt.show()

df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])
df['Mês'] = df['Data da Venda'].dt.month
plt.figure(figsize=(10, 6))
sns.countplot(x='Mês', data=df)
plt.title('Vendas ao longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Número de Vendas')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Região', data=df)
plt.title('Distribuição de Vendas por Região')
plt.xlabel('Região')
plt.ylabel('Número de Vendas')
plt.show()
import pandas as pd

data = {
    'ID do Cliente': ['001', '002', '003', '004', '005', '006', '007', '008', '009'],
    'Data da Venda': ['2023-01-05', '2023-01-10', '2023-01-15', '2023-02-02', '2023-02-10', '2023-02-15', '2024-01-01', '2024-02-02', '2024-01-15'],
    'Valor da Venda': [150, 200, 100, 300, 250, 180, 150, 200, 250],
    'Produto Vendido': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B', 'Produto C', 'Produto C', 'Produto A', 'Produto A'],
    'Canal de Vendas': ['Loja Física', 'Loja Online', 'Loja Física', 'Loja Online', 'Loja Física', 'Loja Online', 'Loja Online', 'Loja Online', 'Loja Online'],
    'Região': ['Norte', 'Sul', 'Nordeste', 'Sudeste', 'Sul', 'Nordeste', 'Sudeste', 'Sudeste', 'Sudeste']
}

df = pd.DataFrame(data)

df.to_csv('dados_vendas.csv', index=False)

print("Conjunto de dados criado e salvo com sucesso em 'dados_vendas.csv'.")

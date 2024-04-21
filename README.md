# Sistema de Análise de Vendas

Bem-vindo ao Sistema de Análise de Vendas. Este projeto consiste em uma ferramenta para análise de dados de vendas, incluindo a geração de um conjunto de dados e análises visuais. Desenvolvido para o processo seletivo 2024 na Linked Empresa Júnior.

## Conteúdo  

1. [Descrição do Projeto](#descrição-do-projeto)  
2. [Instruções de Uso](#instruções-de-uso)  
3. [Dependências](#dependências)  
4. [Configuração](#configuração)   
5. [Contribuições](#contribuições)  
6. [Autores](#autores)  

## Descrição do Projeto  

Este projeto consiste em dois arquivos principais:

1. **criarcsv.py**: Este script Python gera um conjunto de dados de vendas fictício e o salva em um arquivo CSV chamado "dados_vendas.csv".
   
2. **analise.py**: Este script Python realiza análises sobre os dados de vendas contidos no arquivo CSV gerado pelo script anterior. Ele exibe as primeiras linhas do DataFrame, um resumo estatístico das colunas numéricas e gera visualizações gráficas sobre os dados, incluindo a distribuição de vendas por produto, canal de vendas, mês e região.

## Instruções de Uso  

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone o repositório para o seu ambiente local ou baixe os arquivos individualmente.
3. Abra um terminal e navegue até o diretório onde os arquivos estão localizados.
4. Execute o script `criarcsv.py` para gerar o conjunto de dados CSV:
    ```bash
    python criarcsv.py
    ```
   Isso criará um arquivo chamado "dados_vendas.csv" no mesmo diretório.
   Lembrando que nessa parte precisa ter a biblioteca "pandas" instalada.  
5. Em seguida, execute o script `analise.py` para analisar os dados e gerar visualizações:
    ```bash
    python analise.py
    ```
   Isso imprimirá as primeiras linhas do DataFrame, um resumo estatístico das colunas numéricas e exibirá as visualizações gráficas.
   Lembrando que nessa parte precisa ter as bibliotecas "matplotlib" e "seaborn" instalada.  

## Dependências  

- Python 3.x
- Bibliotecas Python: pandas, matplotlib, seaborn

Certifique-se de ter as dependências instaladas antes de executar os scripts.

## Configuração  

Não há configurações adicionais necessárias para executar este projeto.

## Contribuições  

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests com melhorias.

## Autores  

1. [Bernardo Maia Detomi]  

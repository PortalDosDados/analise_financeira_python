# Importando as bibliotecas necessárias
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Definindo os parâmetros para download dos dados
ticker = 'BBAS3.SA'
start_date = '2020-01-01'
end_date = '2023-12-31'

# Baixando os dados históricos do Yahoo Finance
df = yf.download(ticker, start=start_date, end=end_date, interval='1d')

# Ajustando as colunas do DataFrame
df.columns = df.columns.droplevel(1)

# Redefinindo o índice para ser a coluna de datas
df.reset_index(inplace=True)

# Adicionando a coluna Ticker
df['Ticker'] = ticker

# Reordenando para colocar Ticker como primeira coluna
cols = ['Ticker'] + [c for c in df.columns if c != 'Ticker']
df = df[cols]

# Exibindo as primeiras linhas do DataFrame
print(df.head())
# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# Definindo o ticker e o período para download dos dados
ticker = 'BBSE3.SA'
start_date = '2025-01-01'
end_date = '2025-12-31'

# Baixando os dados históricos do Yahoo Finance
df = yf.download(ticker, start=start_date, end=end_date)

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Transformando de MultiIndex para DataFrame simples
df.columns = df.columns.droplevel(1)  # Remover o nível superior do MultiIndex
df.reset_index(inplace=True)           # Transformar índice Date em coluna
df['Ticker'] = ticker            # Adicionar ticker se quiser

# Ordenando as colunas para data, ticker, open, close, high, low, volume
df = df[['Date', 'Ticker', 'Open', 'Close', 'Low', 'High' ,'Volume']]

# Verificando se deu certo a transformação
print(df.head())

# Plotando os dados de preço de fechamento
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Close')
plt.title(f'Preço de Fechamento de {ticker} em 2025')
plt.ylabel('Preço de Fechamento (R$)')
plt.grid()
plt.show()

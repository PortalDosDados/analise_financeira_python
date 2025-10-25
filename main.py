import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

ticker = 'BTC-USD'
start_date = '2020-01-01'
end_date = '2025-12-31'

# Baixando dados
df = yf.download(ticker, start=start_date, end=end_date)

# Remove o nível superior do MultiIndex
df.columns = df.columns.get_level_values(0)
df.reset_index(inplace=True)

df['Ticker'] = ticker
df = df[['Date', 'Ticker', 'Open', 'Close', 'Low', 'High', 'Volume']]

# Média móvel 21 dias
df['MA_21'] = df['Close'].rolling(window=21).mean()

# Média móvel 50 dias
df['MA_50'] = df['Close'].rolling(window=50).mean()

# Média móvel 200 dias
df['MA_200'] = df['Close'].rolling(window=200).mean()

# Exibindo as primeiras linhas do DataFrame
#print(df.head())

# Plot
sns.set_style('whitegrid')
plt.figure(figsize=(12, 6))

sns.lineplot(x=df['Date'], y=df['Close'], label='Preço de Fechamento', color='blue', linewidth=2)
sns.lineplot(x=df['Date'], y=df['MA_21'], label='Média Móvel 21 dias', color='orange', linewidth=2)
#sns.lineplot(x=df['Date'], y=df['MA_50'], label='Média Móvel 50 dias', color='green', linewidth=2)
sns.lineplot(x=df['Date'], y=df['MA_200'], label='Média Móvel 200 dias', color='red', linewidth=2)

plt.title(f'Preço de Fechamento e Média Móvel de {ticker} em 2025', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Preço de Fechamento (USD)', fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import warnings
import matplotlib.dates as mdates

warnings.filterwarnings('ignore')

# Download dos dados
ticker = 'BTC-USD'
start_date = '2024-06-01'
end_date = '2025-10-26'
df = yf.download(ticker, start=start_date, end=end_date)

# Ajuste do MultiIndex
df.columns = df.columns.get_level_values(0)
df.reset_index(inplace=True)
df['Ticker'] = ticker
df = df[['Date', 'Open', 'Close', 'Low', 'High', 'Volume']]

# Médias móveis
df['MA_21'] = df['Close'].rolling(21).mean()
df['MA_50'] = df['Close'].rolling(50).mean()
df['MA_200'] = df['Close'].rolling(200).mean()

# Crossovers MA_21 x MA_50
buy_signals = (df['MA_21'] > df['MA_50']) & (df['MA_21'].shift(1) <= df['MA_50'].shift(1))
sell_signals = (df['MA_21'] < df['MA_50']) & (df['MA_21'].shift(1) >= df['MA_50'].shift(1))

# Definindo cor do volume: verde se alta, vermelho se baixa
df['Volume_Color'] = ['green' if df['Close'][i] >= df['Open'][i] else 'red' for i in range(len(df))]

# Criando figura com dois eixos: preço e volume
fig, ax1 = plt.subplots(figsize=(14,7))

# Preço e médias móveis
sns.lineplot(x=df['Date'], y=df['Close'], ax=ax1, label='Preço de Fechamento', color='blue', linewidth=2)
sns.lineplot(x=df['Date'], y=df['MA_21'], ax=ax1, label='MA 21 dias', color='orange', linewidth=2)
sns.lineplot(x=df['Date'], y=df['MA_50'], ax=ax1, label='MA 50 dias', color='green', linewidth=2)
sns.lineplot(x=df['Date'], y=df['MA_200'], ax=ax1, label='MA 200 dias', color='red', linewidth=2)

# Sinais de compra e venda
ax1.scatter(df['Date'][buy_signals], df['Close'][buy_signals], marker='^', color='green', label='Compra', s=100)
ax1.scatter(df['Date'][sell_signals], df['Close'][sell_signals], marker='v', color='red', label='Venda', s=100)

ax1.set_xlabel('Data', fontsize=12)
ax1.set_ylabel('Preço de Fechamento (USD)', fontsize=12)
ax1.set_title(f'BTC-USD: Preço, Médias Móveis, Volume Colorido e Crossovers', fontsize=16)
ax1.legend(loc='upper left')

# Eixo do volume
ax2 = ax1.twinx()
ax2.bar(df['Date'], df['Volume'], color=df['Volume_Color'], alpha=0.3, label='Volume')
ax2.set_ylabel('Volume', fontsize=12)

# Formatação do eixo X
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.tight_layout()
plt.show()

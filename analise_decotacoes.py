# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# Definindo tickers
tickers = ('^BVSP','BBAS3.SA', 'BBSE3.SA', 'BBDC3.SA', 'SANB3.SA', 'RANI3.SA')
start_date = ('2015-01-01')
end_date = ('2015-12-31')

df =yf.download(tickers, start=start_date, end=end_date)

# Exibindo as 5 primeiras linhas
#print(df.head())

# Cria uma lista de DataFrames individuais, um para cada ticker
dfs = []
for ticker in tickers:
    temp = df.xs(ticker, axis=1, level=1)  # seleciona todas as colunas do ticker
    temp['Ticker'] = ticker                # adiciona coluna do ticker
    dfs.append(temp)

# Concatena todos em um único DataFrame longo
df_longo = pd.concat(dfs).reset_index()

# Reordenando as colunas

df_longo = df_longo[['Date', 'Ticker', 'Close','High', 'Low','Open', 'Volume']]

# Exibindo colunas ajustadas
#print(df_longo.head())


# Salvando em Excel
df_longo.to_excel('cotações.xlsx', index=False)

# Loop para obter dividendos de todos os tickers
df_dividendos = pd.concat(
    [pd.DataFrame({
        'Date': yf.Ticker(t).dividends.index,
        'Dividend': yf.Ticker(t).dividends.values,
        'Ticker': t
    }) for t in tickers]
).reset_index(drop=True)

#print(df_dividendos.head())

# Remove o fuso horário da coluna Date
df_dividendos['Date'] = df_dividendos['Date'].dt.tz_localize(None)

# Arredonda a coluna Dividend para 2 casas decimais
df_dividendos['Dividend'] = df_dividendos['Dividend'].round(2)

# Salvando em Excel
df_dividendos.to_excel('dividendos.xlsx',index=False)
import pandas as pd
import yfinance as yf

# ティッカー
ticker = '^NDX'

# データ取得
yft = yf.Ticker(ticker)
df = yft.history(
  start='2022-12-26', end='2023-12-31',
  auto_adjust=False, actions=True
)

# インデックスを解除・datetimeに変換
df = df.reset_index()
df['Date'] =pd.to_datetime(df['Date'])

# 月末のデータを抽出
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df = df.groupby(['Year','Month']).tail(1)

# 標準出力
print(df)

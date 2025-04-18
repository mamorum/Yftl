import yfinance as yf

# ティッカー
ticker = '^NDX'

# データ取得
yft = yf.Ticker(ticker)
df = yft.history(
  start='2022-12-26', end='2023-12-31',
  auto_adjust=False, actions=True
)

# 月末のデータを抽出
df['Year'] = df.index.year
df['Month'] = df.index.month
df = df.groupby(['Year','Month']).tail(1)

# 標準出力
print(df)

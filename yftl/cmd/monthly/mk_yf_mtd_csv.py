import yfinance as yf

# 取得する月間収益率
ticker = '^SPX'
start = 2022
end = 2024

# 日次データの範囲（少し余分に）
symd = f'{start-1}-12-20'
eymd = f'{end+1}-01-10'

# 日次データを取得（昇順）
yft = yf.Ticker(ticker)
df = yft.history(
  start=symd, end=eymd,
  auto_adjust=False, actions=False
)

# 月末のデータを抽出
df['Year'] = df.index.year
df['Month'] = df.index.month
df = df.groupby(['Year','Month']).tail(1)
df = df[['Close']]  # 日付と終値を残す
df = df.iloc[:-1]  # 不要な1月分を削除

# 月間収益率を算出
df['MTD'] = df['Close'].pct_change()

# 行を逆順に変更（降順）
df = df.iloc[::-1]

# CSVに出力
fmt = '%Y-%m-%d'
df.to_csv('spx-mtd.csv', date_format=fmt)

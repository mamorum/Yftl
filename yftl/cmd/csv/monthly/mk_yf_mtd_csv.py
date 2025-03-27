# 使用例
# > python cmd\monthly\mk_yf_mtd_csv.py ^^SPX 2022 2023
# > python cmd\monthly\mk_yf_mtd_csv.py JPY=X 2023 2023

import sys
import yfinance as yf
import lib.ticker as lticker

# コマンドライン引数の取得
ticker = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

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

# 出力ファイルを決定
lticker = lticker.lower(ticker)
csvfile = f'{lticker}-mtd-{start}-{end}.csv'

# CSVに出力
fmt = '%Y-%m-%d'
df.to_csv(csvfile, date_format=fmt)

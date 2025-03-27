# 使用例
# > python cmd\daily\mk_yf_daily_ytd_csv ^^SPX 2022 2023
# > python cmd\daily\mk_yf_daily_ytd_csv JPY=X 2023 2023

import sys
import pandas as pd
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

# 開始年-1の年末終値を抽出
idf = df[df.index.year == start-1]
idate = idf.index.max()
iclose = idf.loc[idate, 'Close']

# 開始年～終了年のデータを抽出
df = df.loc[f'{start}-01-01':f'{end}-12-31']
df = df[['Close']]  # 日付と終値を残す

# 日次の年初来を算出
df['YTD'] = df['Close'] / iclose - 1 

# 行を逆順に変更（降順）
df = df.iloc[::-1]

# 出力ファイルを決定
lticker = lticker.lower(ticker)
csvfile = f'{lticker}-daily-ytd-{start}-{end}.csv'

# CSVに出力
fmt = '%Y-%m-%d'
df.to_csv(csvfile, date_format=fmt)

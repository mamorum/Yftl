# 使用例
# > python cmd\csv\daily\mk_yf_dtd_csv.py ^^SPX 2022 2023
# > python cmd\csv\daily\mk_yf_dtd_csv.py JPY=X 2023 2023

import sys
import pandas as pd
import yfinance as yf
import lib.ticker as lticker

def _dtd_df(ticker: str, year: int) -> pd.DataFrame:
  # 日次データの範囲（少し余分に）
  symd = f'{year-1}-12-20'
  eymd = f'{year+1}-01-10'
  # 日次データを取得（昇順）
  yft = yf.Ticker(ticker)
  df = yft.history(
    start=symd, end=eymd,
    auto_adjust=False, actions=False
  )
  # 開始年-1の年末を抽出
  idf = df[df.index.year == year-1]
  idate = idf.index.max()
  idf = idf.loc[[idate]]
  # 開始年～終了年のデータを抽出
  df = df.loc[f'{year}-01-01':f'{year}-12-31']
  # 抽出したデータを結合
  df = pd.concat([idf, df])
  df = df[['Close']]  # 日付と終値を残す
  # 日次の収益率を算出
  df['DTD'] = df['Close'].pct_change()
  return df


# 処理開始
# コマンドライン引数の取得
ticker = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

for year in range(start, end+1):
  df = _dtd_df(ticker, year)
  # 行を逆順に変更（降順）
  df = df.iloc[::-1]
  # 出力ファイルを決定
  lt = lticker.lower(ticker)
  csvfile = f'{lt}-dtd-{year}.csv'
  # CSVに出力
  fmt = '%Y-%m-%d'
  df.to_csv(csvfile, date_format=fmt)

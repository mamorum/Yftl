# 使用例
# > python cmd\plt\daily\plt_yf_daily_ytd.py ^^SPX 2022 2023
# > python cmd\plt\daily\plt_yf_daily_ytd.py ^^SPX,^^NDX 2023 2023

import sys
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

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

# リターンを算出（パーセント）
df['RTN'] = (df['Close'] / iclose - 1) * 100

# 1月1日を補完
jan1 = pd.Timestamp(f"{start}-01-01 00:00:00-0500", tz="America/New_York")
jan1_df = pd.DataFrame({'Date': [jan1], 'Close': [0], 'RTN': [0]})
jan1_df.set_index('Date', inplace=True)
df = pd.concat([jan1_df, df])

# グラフを作成
plt.figure(figsize=(12, 6))

# 年初来の推移をプロット
plt.plot(df.index, df["RTN"], label=ticker)

# グラフのラベルとタイトル
plt.xlabel("Date (Months)")
plt.ylabel("Return (%)")
plt.title("Performance")
plt.legend()
plt.grid()

# グラフを表示
plt.tight_layout()
plt.show()

# 使用例
# > python cmd\plt\daily\plt_yf_daily_rtn.py ^^SPX,^^NDX 2022 2023
# > python cmd\plt\daily\plt_yf_daily_rtn.py ^^SPX,^^NDX 2023 2023

import sys
import matplotlib.pyplot as plt
import lib.yfi as lyf

# コマンドライン引数の取得
tickers = sys.argv[1].split(',')
start = int(sys.argv[2])
end = int(sys.argv[3])

# グラフを作成
plt.figure(figsize=(12, 6))

# リターンの推移をプロット
for ticker in tickers:
  df = lyf.rtn_df(ticker, start, end)
  plt.plot(df.index, df["RTN"], label=ticker)

# グラフのラベルとタイトル
plt.xlabel("Date")
plt.ylabel("Return (%)")
plt.title("Performance")
plt.legend()
plt.grid()

# グラフを表示
plt.tight_layout()
plt.show()

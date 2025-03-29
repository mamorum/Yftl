import yfinance as yf
import pandas as pd

# データ取得
yt = yf.Ticker("^SPX")  # 銘柄を指定
data = yt.history(
  start="2020-01-01", end="2025-01-01",
  auto_adjust=False
)

# 年末の終値を取得
data['Year'] = data.index.year
yearly_close = data.groupby('Year')['Close'].last()  # 年末の終値を抽出
final_price = yearly_close.iloc[-1]  # 最後の年末の終値

rtns = []
for price in yearly_close[:-1]:  # 最後の年を除いて処理
    rtn = final_price / price - 1
    rtns.append(rtn)

return_rate = (sum(rtns) / len(rtns)) * 100  # 収益率

# 結果表示
print(f"収益率: {return_rate:.2f}%")


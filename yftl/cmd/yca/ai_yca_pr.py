import yfinance as yf
import pandas as pd

# 1. yfinanceデータの取得（例: SPY）
ticker = yf.Ticker("^SPX")
data = ticker.history(
  start="2020-12-26", end="2024-01-10",
  auto_adjust=False, actions=True
)

# 年末データを抽出
data['Year'] = data.index.year
data['Month'] = data.index.month
year_end = data[(data['Month'] == 12)].groupby('Year').tail(1)  # 年末の終値
# 毎年一定金額を投資
investment_per_year = 1000  # 毎年の投資額
year_end['Investment'] = investment_per_year

# 累積元本の計算
year_end['Cumulative_Principal'] = year_end['Investment'].cumsum()

# 年初の元本を計算（前年末の累積元本を基準にする）
year_end['Start_Principal'] = year_end['Cumulative_Principal'].shift(1).fillna(0)

# ポートフォリオ評価額の計算
year_end['Units'] = year_end['Investment'] / year_end['Close']  # 購入単位
year_end['Cumulative_Units'] = year_end['Units'].cumsum()  # 累積単位
year_end['Portfolio_Value'] = year_end['Cumulative_Units'] * year_end['Close']  # 評価額

# 年末リターンを計算（前年末の元本に対する増加率）
year_end['Return'] = (year_end['Portfolio_Value'] / year_end['Start_Principal']) - 1

# 7. 結果を表示
print(year_end[['Close', 'Cumulative_Principal', 'Start_Principal', 'Units', 'Cumulative_Units', 'Portfolio_Value', 'Return']])

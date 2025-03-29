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

# 毎年末に一定額を投資
initial_investment = 1000  # 毎年末に投資する金額
total_shares = 0  # 保有する株数
total_invested = 0  # 総投資額

for price in yearly_close:  # 各年の終値に基づいて株を購入
    shares = initial_investment / price  # 購入可能な株数
    total_shares += shares
    total_invested += initial_investment

# 最終的なポートフォリオ価値
final_price = yearly_close.iloc[-1]  # 最後の年末の終値
portfolio_value = total_shares * final_price  # 総株数 × 最終価格

# 収益率を計算
profit = portfolio_value - total_invested  # 総利益
return_rate = (profit / total_invested) * 100  # 収益率

# 結果表示
print(f"総投資額: {total_invested:.2f} USD")
print(f"最終ポートフォリオ価値: {portfolio_value:.2f} USD")
print(f"収益率: {return_rate:.2f}%")


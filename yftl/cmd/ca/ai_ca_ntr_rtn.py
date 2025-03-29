import yfinance as yf

# データ取得
ticker = "SPY"  # 指数を指定（例: S&P 500 Index）
yt = yf.Ticker(ticker)
data = yt.history(
 start="2020-01-01", end="2025-01-01",
 auto_adjust=False
)
dividends = yt.dividends  # 分配金情報の取得

# 初期設定
investment_years = [2022, 2023]  # 投資開始年
results = []  # 各年ごとのリターンを格納

for start_year in investment_years:
    # その年末に購入
    start_price = data[data.index.year == start_year].iloc[-1]['Close']
    shares = 1.0  # 初期購入量（1口）
    
    for index, row in data.iterrows():
        year = index.year
        if year > start_year:
            # 分配金再投資
            if index in dividends.index:  # 分配金がある日
                dividend = dividends.loc[index]
                print(dividend)
                reinvest_price = row['Close']  # 再投資時点の株価
                shares += dividend / reinvest_price  # 保有口数を更新

    # 最終リターンの計算
    end_price = data[data.index.year == 2024].iloc[-1]['Close']  # 2024年末の終値
    portfolio_value = shares * end_price
    initial_investment_value = 1.0 * start_price
    return_rate = (portfolio_value - initial_investment_value) / initial_investment_value
    results.append(return_rate * 100)

# 平均リターンの計算
average_return = sum(results) / len(results)

# 結果出力
print(f"各年のリターン: {results}")
print(f"平均リターン: {average_return:.2f}%")

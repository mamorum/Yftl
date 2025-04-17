import matplotlib.pyplot as plt
import yfinance as yf

# ティッカー
ticker = '^SPX'

# データ取得・リターン算出
yft = yf.Ticker(ticker)
df = yft.history(
  start='2023-12-29', end='2024-12-31',
  auto_adjust=False, actions=True
)
iclose = df.iloc[0]['Close']
df['RTN'] = df['Close'] / iclose - 1

# グラフのフォント設定
plt.rcParams['font.family'] = 'Yu Gothic'

# グラフを作成（リターンの単位を%に変更）
plt.figure(figsize=(9.6, 5.4))
plt.plot(df.index, df['RTN'] * 100, label='SPX')

# グラフの設定
plt.title('SPX 2024年')
plt.xlabel('営業日')
plt.ylabel('リターン (%)')
plt.legend()
plt.grid()
plt.tight_layout()

# グラフを保存
plt.savefig('spx-rtn-2024.png', format='png')

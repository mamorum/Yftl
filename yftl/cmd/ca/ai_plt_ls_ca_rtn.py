import matplotlib.pyplot as plt
import pandas as pd

# 例のデータ（適切なデータを投入してください）
dates = pd.date_range(start="2020-01-01", end="2025-01-01", freq="M")
lump_sum = [100000 * (1 + 0.01)**i for i in range(len(dates))]
dca = [1000 * sum((1 + 0.01)**j for j in range(i+1)) for i in range(len(dates))]

# グラフ作成
plt.figure(figsize=(10, 6))
plt.plot(dates, lump_sum, label="一括投資 (Lump Sum)")
plt.plot(dates, dca, label="積立投資 (Dollar-Cost Averaging)")
plt.title("一括投資と積立投資の累積資産推移")
plt.xlabel("日付")
plt.ylabel("資産価値")
plt.legend()
plt.grid()
plt.show()


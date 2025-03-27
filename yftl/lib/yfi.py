import pandas as pd
import yfinance as yf

def _hist_df(ticker: str, start: int, end: int) -> pd.DataFrame:
  # 日次データの範囲（少し余分に）
  symd = f'{start-1}-12-20'
  eymd = f'{end+1}-01-10'
  # 日次データを取得（昇順）
  yft = yf.Ticker(ticker)
  df = yft.history(
    start=symd, end=eymd,
    auto_adjust=False, actions=False
  )
  return df

def _jan1(year: int) -> pd.Timestamp:  
  jan1ts = f"{year}-01-01 00:00:00-0500"
  timezone = "America/New_York"
  jan1 = pd.Timestamp(jan1ts, tz=timezone)
  return jan1

def rtn_df(ticker: str, start: int, end: int) -> pd.DataFrame:
  # データをダウンロード
  df = _hist_df(ticker, start, end)
  # 開始年-1の年末終値を抽出
  idf = df[df.index.year == start-1]
  idate = idf.index.max()
  iclose = idf.loc[idate, 'Close']
  # 開始年～終了年のデータを抽出
  df = df.loc[f'{start}-01-01':f'{end}-12-31']
  # リターンを算出（パーセント）
  df['RTN'] = (df['Close'] / iclose - 1) * 100
  # インデックスの日付とリターンを残す
  df = df[['RTN']]
  # 1月1日を収益率0%で補完
  jan1 = _jan1(start)
  jan1_df = pd.DataFrame({'Date': [jan1], 'RTN': [0]})
  jan1_df.set_index('Date', inplace=True)
  df = pd.concat([jan1_df, df])
  return df

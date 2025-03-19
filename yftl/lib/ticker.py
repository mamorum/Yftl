def lower(ticker):
  ticker = ticker.replace("^", "")
  ticker = ticker.replace("=", "")
  ticker = ticker.lower()
  return ticker

def get_stock(stock):
  stock = vnstock.stock_historical_data(stock,'2018-01-01', '2023-01-01')
  stock.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Vol', 'Ticker']
  stock['Date'] = pd.to_datetime(stock['Date'])
  stock.sort_values('Date', ascending=True, inplace=True)
  return stock

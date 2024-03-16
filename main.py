import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol] <= quantity:
                del self.stocks[symbol]
            else:
                self.stocks[symbol] -= quantity

    def track_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            stock = yf.Ticker(symbol)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            total_value += current_price * quantity
            print(f"{symbol}: {quantity} shares - Current Price: {current_price:.2f} - Total Value: {current_price * quantity:.2f}")
        print(f"Total Portfolio Value: {total_value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)
    portfolio.add_stock("MSFT", 8)

    portfolio.track_portfolio_value()

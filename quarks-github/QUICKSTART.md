# Quick Start Guide

Get Quarks up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for downloading stock data)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/quarks-backtester.git
cd quarks-backtester
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

If you get permission errors, use:
```bash
pip install --user -r requirements.txt
```

Or on some systems:
```bash
pip3 install -r requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

You should see:
```
🚀 Starting Quarks Backtesting PRO Server...
📊 11 Strategies Available (10 + Custom Builder)
📈 Enhanced Charts with Buy/Sell Markers
🔍 Zoom & Pan Enabled
🌐 Open http://localhost:5000
 * Running on http://0.0.0.0:5000
```

### Step 4: Open in Browser

Open your web browser and go to:
```
http://localhost:5000
```

## Your First Backtest

1. **Enter Stock Ticker**
   - Type: `AAPL` (or any valid stock ticker)

2. **Select Date Range**
   - Start: `2020-01-01`
   - End: `2023-01-01`

3. **Choose Strategy**
   - Select: `SMA Crossover (10/30)`

4. **Configure Settings** (optional)
   - Initial Cash: `$100,000`
   - Commission: `0.001` (0.1%)
   - Position Sizing: `Percentage` at `95%`

5. **Run Backtest**
   - Click the blue "🚀 Run Backtest" button
   - Wait 2-5 seconds for results

## Understanding Your Results

### Metrics Card
- **Total Return**: Your profit/loss in $ and %
- **Sharpe Ratio**: Risk-adjusted returns (higher is better)
- **Max Drawdown**: Largest loss from peak
- **Win Rate**: Percentage of profitable trades

### Interactive Chart
- **Blue Line**: Stock price over time
- **Green Line**: Your portfolio value
- **Green Triangles**: Buy signals (▲)
- **Red Triangles**: Sell signals (▼)

### Chart Controls
- **Scroll**: Zoom in/out
- **Drag**: Pan left/right
- **Click Buttons**: Toggle visibility
- **Reset Zoom**: Return to full view

## Next Steps

### Try Different Strategies
1. Click the strategy dropdown
2. Select a different strategy (try RSI or MACD)
3. Run another backtest
4. Compare results

### Build a Custom Strategy
1. Select "🔧 Custom Strategy"
2. Choose indicator (SMA, EMA, or RSI)
3. Set your periods
4. Run backtest

### Test Different Stocks
Popular tickers to try:
- **AAPL** - Apple (stable)
- **TSLA** - Tesla (volatile)
- **MSFT** - Microsoft (tech giant)
- **SPY** - S&P 500 ETF (market benchmark)
- **NVDA** - Nvidia (growth stock)

### Experiment with Position Sizing
1. Change "Position Sizing" dropdown
2. Try:
   - **All-In**: Use 100% of capital
   - **Fixed Amount**: Invest exact $10,000
   - **Fixed Shares**: Buy exact 100 shares

## Common Issues

### "Module not found"
```bash
pip install flask flask-cors backtrader yfinance pandas
```

### Port 5000 in use
Edit last line of `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Change to 8000
```

### No data for ticker
- Check ticker spelling (should be uppercase)
- Try a different ticker
- Verify date range is valid

### Chart not loading
- Refresh page (Ctrl+R or Cmd+R)
- Clear cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check browser console (F12) for errors

## Tips for Success

1. **Start Simple**
   - Use AAPL with default settings
   - Learn the interface
   - Understand the metrics

2. **Test Multiple Periods**
   - Bull market: 2019-2021
   - Bear market: 2022
   - Full cycle: 2020-2023

3. **Compare Strategies**
   - Run same ticker with different strategies
   - Screenshot results
   - Analyze which works best

4. **Use Buy & Hold as Baseline**
   - Always compare to passive investing
   - Check if active trading adds value

5. **Watch for Overfitting**
   - Test on different time periods
   - Use out-of-sample data
   - Don't optimize too much

## Getting Help

- **Documentation**: Check the `docs/` folder
- **Issues**: Open a GitHub issue
- **Community**: Join discussions
- **Email**: Contact maintainer

## What's Next?

Once you're comfortable with basics:

1. Read [STRATEGIES.md](docs/STRATEGIES.md) - Learn each strategy
2. Check [API.md](docs/API.md) - Use programmatically
3. See [DEPLOYMENT.md](docs/DEPLOYMENT.md) - Deploy online
4. Review [CONTRIBUTING.md](CONTRIBUTING.md) - Contribute code

## Resources

- [Backtrader Documentation](https://www.backtrader.com/docu/)
- [Technical Analysis Basics](https://www.investopedia.com/technical-analysis-4689657)
- [Position Sizing Guide](https://www.investopedia.com/articles/trading/09/determine-position-size.asp)

---

**Congratulations!** You're now ready to backtest trading strategies like a pro! 🎉

Happy backtesting! 📈

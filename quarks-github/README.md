# ⚛️ Quarks - Professional Stock Backtesting Platform

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A professional-grade stock backtesting platform with 11 trading strategies, custom strategy builder, interactive charts with zoom/pan capabilities, and comprehensive performance metrics.

## ✨ Features

### 🎯 11 Trading Strategies
- **SMA Crossover** - Simple Moving Average crossover (10/30)
- **EMA Crossover** - Exponential Moving Average crossover (9/21)
- **RSI Strategy** - Relative Strength Index (30/70)
- **MACD Strategy** - Moving Average Convergence Divergence
- **Bollinger Bands** - Buy lower band, sell upper band
- **Stochastic Oscillator** - Momentum indicator (20/80)
- **Momentum Strategy** - Price momentum indicator
- **Triple SMA** - Three moving average alignment (5/15/30)
- **Mean Reversion** - Trade on deviation from mean
- **Buy & Hold** - Baseline comparison
- **Custom Strategy Builder** - Build your own strategy with customizable indicators

### 📊 Interactive Charts
- **Zoom & Pan** - Scroll to zoom, drag to pan
- **Buy/Sell Markers** - Visual trade signals on chart
- **Portfolio Tracking** - Real-time portfolio value overlay
- **Toggle Controls** - Show/hide any chart element
- **Dual Y-Axis** - Price and portfolio on separate axes
- **Responsive Design** - Works on desktop and mobile

### 🎛️ Position Sizing
- Percentage of Portfolio (default 95%)
- All-In (100%)
- Fixed Dollar Amount
- Fixed Number of Shares

### 📈 Comprehensive Metrics
- Total Return ($ and %)
- Sharpe Ratio
- Maximum Drawdown
- Win Rate
- Total Trades
- Winning/Losing Trades
- Average Trade P/L

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/quarks-backtester.git
cd quarks-backtester
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser**
```
http://localhost:5000
```

That's it! 🎉

## 📖 Usage

### Running Your First Backtest

1. Enter a stock ticker (e.g., AAPL, MSFT, TSLA)
2. Select date range (start and end dates)
3. Choose a trading strategy
4. Configure position sizing
5. Set initial cash and commission
6. Click "Run Backtest"
7. Analyze results with interactive charts

### Using the Custom Strategy Builder

1. Select "Custom Strategy" from the dropdown
2. Choose your indicator (SMA, EMA, or RSI)
3. Set period values
4. Run backtest with your custom parameters

### Chart Controls

- **Zoom**: Scroll mouse wheel on chart
- **Pan**: Click and drag on chart
- **Toggle**: Click buttons to show/hide elements
- **Reset**: Click "Reset Zoom" to restore original view

## 🏗️ Architecture

### Backend (Python/Flask)
```
app.py
├── Strategy Classes (11 strategies)
├── Position Sizers (4 types)
├── Backtrader Integration
├── Yahoo Finance Data Fetching
└── REST API Endpoint
```

### Frontend (HTML/JavaScript)
```
index.html
├── Chart.js for visualization
├── Zoom/Pan plugins
├── Toggle controls
└── Responsive UI
```

## 📦 Dependencies

- **Flask** - Web framework
- **Flask-CORS** - Cross-origin support
- **Backtrader** - Backtesting engine
- **yfinance** - Stock data fetching
- **pandas** - Data manipulation
- **Chart.js** - Interactive charts
- **chartjs-plugin-zoom** - Zoom functionality

## 🎨 Screenshots

### Main Dashboard
![Dashboard](screenshots/dashboard.png)

### Interactive Chart with Markers
![Chart](screenshots/chart.png)

### Results Metrics
![Metrics](screenshots/metrics.png)

*(Add actual screenshots to the `screenshots/` directory)*

## 🛠️ Configuration

### Changing the Port
Edit the last line of `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your port
```

### Adding Custom Strategies
1. Create a new strategy class in `app.py` inheriting from `BaseStrategy`
2. Add it to the `STRATEGIES` dictionary
3. Add the option to the dropdown in `index.html`

### Modifying Default Parameters
Edit the strategy class parameters in `app.py`:
```python
class SMAStrategy(BaseStrategy):
    params = (('short_period', 10), ('long_period', 30))  # Modify these
```

## 🧪 Testing

Run a quick test:
```bash
# Start the server
python app.py

# In your browser, go to http://localhost:5000
# Run a backtest with:
Ticker: AAPL
Dates: 2020-01-01 to 2023-01-01
Strategy: SMA Crossover
```

## 📊 Performance

- **Backtest Execution**: 2-5 seconds
- **Chart Rendering**: Instant
- **Data Points**: Handles 1000+ efficiently
- **Memory Usage**: ~50-100MB
- **Concurrent Users**: Supports multiple

## 🐛 Troubleshooting

### "Module not found" Error
```bash
pip install --break-system-packages flask flask-cors backtrader yfinance pandas
```

### Port 5000 Already in Use
Change the port in `app.py` (last line) to 8000 or any available port.

### Chart Not Loading
- Clear browser cache (Ctrl+Shift+R)
- Check browser console for errors (F12)
- Ensure Chart.js CDN is accessible

### No Data for Ticker
- Verify ticker symbol is correct
- Check date range is valid
- Try a different ticker (AAPL, MSFT work reliably)

## 🚀 Deployment

### Deploy to Railway
1. Push code to GitHub
2. Connect Railway to your repository
3. Railway auto-deploys!

### Deploy to Heroku
```bash
# Create Procfile
echo "web: python app.py" > Procfile

# Deploy
git push heroku main
```

### Deploy to Render
1. Connect GitHub repository
2. Select Python environment
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Backtrader](https://www.backtrader.com/) - Powerful backtesting framework
- [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo Finance data
- [Chart.js](https://www.chartjs.org/) - Beautiful charts
- [Flask](https://flask.palletsprojects.com/) - Lightweight web framework

## 📧 Contact

- **Author**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Project Link**: [https://github.com/yourusername/quarks-backtester](https://github.com/yourusername/quarks-backtester)

## ⭐ Star History

If you find this project useful, please consider giving it a star!

## 🗺️ Roadmap

- [ ] Add more technical indicators (Williams %R, ATR, etc.)
- [ ] Machine learning strategy optimizer
- [ ] Portfolio optimization
- [ ] Multi-asset backtesting
- [ ] Export results to CSV/PDF
- [ ] Historical performance comparison
- [ ] Real-time trading integration
- [ ] Strategy parameter optimization
- [ ] Monte Carlo simulation
- [ ] Walk-forward analysis

## 📚 Documentation

For detailed documentation, visit the [docs](docs/) folder:
- [Strategy Guide](docs/STRATEGIES.md)
- [API Reference](docs/API.md)
- [Chart Features](docs/CHARTS.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 💰 Support

If you find this project helpful, consider supporting its development:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-yellow.svg)](https://buymeacoffee.com/yourusername)

---

Made with ❤️ and ☕ by [Your Name]

**Happy Backtesting!** 🚀📈

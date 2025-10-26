# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-10-26

### Added
- Initial release of Quarks Backtester
- 11 trading strategies (10 pre-built + custom builder)
- Interactive Chart.js charts with zoom and pan
- Buy/Sell signal markers on charts
- Portfolio value tracking overlay
- Toggle controls for chart elements
- Dual Y-axis (price and portfolio)
- 4 position sizing methods
- Comprehensive performance metrics
- Sharpe ratio calculation
- Maximum drawdown tracking
- Win rate statistics
- Real-time data from Yahoo Finance
- Flask REST API backend
- Responsive web interface
- Dark professional theme
- Custom strategy builder
- Mobile responsive design

### Features
- **Strategies:** SMA Crossover, EMA Crossover, RSI, MACD, Bollinger Bands, Stochastic, Momentum, Triple SMA, Mean Reversion, Buy & Hold, Custom
- **Position Sizing:** Percentage, All-In, Fixed Amount, Fixed Shares
- **Charts:** Interactive zoom/pan, buy/sell markers, portfolio overlay
- **Metrics:** Total return, Sharpe ratio, max drawdown, win rate, trade statistics

### Technical
- Python 3.8+ backend
- Flask web framework
- Backtrader backtesting engine
- Chart.js for visualization
- yfinance for data
- Pandas for data manipulation

## [Unreleased]

### Planned
- More technical indicators (Williams %R, ATR, etc.)
- Strategy parameter optimization
- Multi-asset backtesting
- Export results to CSV/PDF
- Monte Carlo simulation
- Walk-forward analysis
- Machine learning integration
- Real-time trading integration
- Portfolio optimization
- Risk management tools

---

## Version History

### v1.0.0 - Initial Release
First stable release with core backtesting functionality

---

For older releases and detailed changes, see the [releases page](https://github.com/yourusername/quarks-backtester/releases).

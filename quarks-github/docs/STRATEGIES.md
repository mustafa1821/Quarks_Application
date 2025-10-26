# Trading Strategies Guide

This document provides detailed information about each trading strategy available in Quarks.

## 1. SMA Crossover Strategy

**Type:** Trend Following  
**Default Parameters:** Short: 10, Long: 30

### How It Works
- Calculates two Simple Moving Averages with different periods
- **Buy Signal:** When short SMA crosses above long SMA
- **Sell Signal:** When short SMA crosses below long SMA

### Best For
- Trending markets
- Long-term positions
- Lower frequency trading

### Parameters
- `short_period`: Number of days for short moving average (default: 10)
- `long_period`: Number of days for long moving average (default: 30)

---

## 2. EMA Crossover Strategy

**Type:** Trend Following  
**Default Parameters:** Short: 9, Long: 21

### How It Works
- Similar to SMA but uses Exponential Moving Averages
- Gives more weight to recent prices
- **Buy Signal:** When short EMA crosses above long EMA
- **Sell Signal:** When short EMA crosses below long EMA

### Best For
- More responsive to price changes than SMA
- Medium-term positions
- Volatile markets

### Parameters
- `short_period`: Short EMA period (default: 9)
- `long_period`: Long EMA period (default: 21)

---

## 3. RSI Strategy

**Type:** Mean Reversion  
**Default Parameters:** Period: 14, Oversold: 30, Overbought: 70

### How It Works
- Uses Relative Strength Index to identify overbought/oversold conditions
- **Buy Signal:** When RSI falls below oversold threshold
- **Sell Signal:** When RSI rises above overbought threshold

### Best For
- Range-bound markets
- Short to medium-term trading
- High volatility stocks

### Parameters
- `period`: RSI calculation period (default: 14)
- `oversold`: Buy threshold (default: 30)
- `overbought`: Sell threshold (default: 70)

---

## 4. MACD Strategy

**Type:** Momentum  
**Default Parameters:** Fast: 12, Slow: 26, Signal: 9

### How It Works
- Uses Moving Average Convergence Divergence
- **Buy Signal:** When MACD line crosses above signal line
- **Sell Signal:** When MACD line crosses below signal line

### Best For
- Trending markets
- Momentum trading
- Medium-term positions

### Parameters
- `fast`: Fast EMA period (default: 12)
- `slow`: Slow EMA period (default: 26)
- `signal`: Signal line period (default: 9)

---

## 5. Bollinger Bands Strategy

**Type:** Mean Reversion  
**Default Parameters:** Period: 20, Std Dev: 2

### How It Works
- Uses standard deviation bands around a moving average
- **Buy Signal:** When price touches or crosses below lower band
- **Sell Signal:** When price touches or crosses above upper band

### Best For
- Range-bound markets
- Identifying overbought/oversold
- Short to medium-term trading

### Parameters
- `period`: Moving average period (default: 20)
- `devfactor`: Standard deviations (default: 2)

---

## 6. Stochastic Oscillator Strategy

**Type:** Momentum  
**Default Parameters:** Period: 14, Oversold: 20, Overbought: 80

### How It Works
- Compares current price to price range over a period
- **Buy Signal:** When %K falls below oversold threshold
- **Sell Signal:** When %K rises above overbought threshold

### Best For
- Identifying turning points
- Range-bound markets
- Short-term trading

### Parameters
- `period`: Lookback period (default: 14)
- `oversold`: Buy threshold (default: 20)
- `overbought`: Sell threshold (default: 80)

---

## 7. Momentum Strategy

**Type:** Momentum  
**Default Parameters:** Period: 10

### How It Works
- Measures rate of price change
- **Buy Signal:** When momentum turns positive
- **Sell Signal:** When momentum turns negative

### Best For
- Trending markets
- Catching strong moves
- Medium-term trading

### Parameters
- `period`: Momentum calculation period (default: 10)

---

## 8. Triple SMA Strategy

**Type:** Trend Following  
**Default Parameters:** Short: 5, Medium: 15, Long: 30

### How It Works
- Uses three moving averages for confirmation
- **Buy Signal:** When short > medium > long (all aligned bullish)
- **Sell Signal:** When alignment breaks

### Best For
- Strong trending markets
- High confidence trades
- Lower frequency but higher quality signals

### Parameters
- `short`: Short SMA period (default: 5)
- `medium`: Medium SMA period (default: 15)
- `long`: Long SMA period (default: 30)

---

## 9. Mean Reversion Strategy

**Type:** Mean Reversion  
**Default Parameters:** Period: 20, Threshold: 2

### How It Works
- Identifies when price deviates significantly from average
- **Buy Signal:** When price is >2 std devs below average
- **Sell Signal:** When price is >2 std devs above average

### Best For
- Range-bound markets
- High volatility stocks
- Short-term trading

### Parameters
- `period`: Moving average period (default: 20)
- `threshold`: Standard deviation threshold (default: 2)

---

## 10. Buy & Hold Strategy

**Type:** Passive  
**Parameters:** None

### How It Works
- Simply buys at the start and holds until the end
- No active trading decisions
- Used as a baseline for comparison

### Best For
- Long-term investing
- Comparison benchmark
- Bull markets

---

## 11. Custom Strategy Builder

**Type:** Customizable  
**Parameters:** User-defined

### How It Works
- Choose indicator: SMA, EMA, or RSI
- Set your own periods
- Define your buy/sell logic

### Best For
- Testing custom ideas
- Finding optimal parameters
- Experimentation

### Available Indicators
- **SMA/EMA:** Crossover logic
- **RSI:** Oversold/overbought logic

---

## Strategy Selection Guide

### For Trending Markets
1. SMA Crossover
2. EMA Crossover
3. MACD
4. Triple SMA

### For Range-Bound Markets
1. RSI
2. Bollinger Bands
3. Mean Reversion
4. Stochastic

### For High Volatility
1. RSI
2. Bollinger Bands
3. Stochastic

### For Low Volatility
1. SMA Crossover
2. Buy & Hold

---

## Tips for Success

1. **Test Multiple Strategies** - Different strategies work better in different market conditions
2. **Use Appropriate Timeframes** - Match strategy frequency with your goals
3. **Consider Commission Costs** - High-frequency strategies may be hurt by commissions
4. **Compare to Buy & Hold** - Always benchmark against passive investing
5. **Backtest Multiple Periods** - Test in both bull and bear markets
6. **Use Stop Losses** - Consider adding risk management (future feature)

---

## Performance Metrics

When evaluating strategies, focus on:

- **Total Return %** - Overall profitability
- **Sharpe Ratio** - Risk-adjusted returns (higher is better)
- **Max Drawdown** - Largest peak-to-trough decline (lower is better)
- **Win Rate** - Percentage of profitable trades
- **Total Trades** - How active the strategy is

---

## Future Strategies (Roadmap)

- Williams %R
- ATR-based strategies
- Ichimoku Cloud
- Parabolic SAR
- Volume-based strategies
- Machine learning strategies

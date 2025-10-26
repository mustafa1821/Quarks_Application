# API Reference

Quarks provides a REST API for running backtests programmatically.

## Base URL

```
http://localhost:5000
```

## Endpoints

### POST /api/backtest

Run a backtest with specified parameters.

#### Request

**Method:** `POST`  
**Content-Type:** `application/json`

**Body Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| ticker | string | Yes | - | Stock ticker symbol (e.g., "AAPL") |
| start_date | string | Yes | - | Start date (YYYY-MM-DD) |
| end_date | string | Yes | - | End date (YYYY-MM-DD) |
| strategy | string | Yes | - | Strategy ID (see list below) |
| initial_cash | number | No | 100000 | Starting capital |
| commission | number | No | 0.001 | Commission rate (0.001 = 0.1%) |
| position_sizing | string | No | "percent" | Position sizing method |
| position_value | number | No | 95 | Size value (depends on method) |
| custom_params | object | No | {} | Custom strategy parameters |

**Strategy IDs:**
- `sma-crossover`
- `ema-crossover`
- `rsi`
- `macd`
- `bollinger`
- `stochastic`
- `momentum`
- `triple-sma`
- `mean-reversion`
- `buy-hold`
- `custom`

**Position Sizing Methods:**
- `percent` - Percentage of portfolio (position_value = 1-100)
- `all-in` - Use all available cash
- `fixed-amount` - Fixed dollar amount (position_value = dollar amount)
- `fixed-shares` - Fixed number of shares (position_value = share count)

#### Example Request

```bash
curl -X POST http://localhost:5000/api/backtest \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "AAPL",
    "start_date": "2020-01-01",
    "end_date": "2023-01-01",
    "strategy": "sma-crossover",
    "initial_cash": 100000,
    "commission": 0.001,
    "position_sizing": "percent",
    "position_value": 95
  }'
```

#### Response

**Success (200 OK):**

```json
{
  "success": true,
  "portfolio": {
    "starting_value": 100000.0,
    "ending_value": 145230.50,
    "total_return": 45230.50,
    "total_return_pct": 45.23
  },
  "metrics": {
    "sharpe_ratio": 1.234,
    "max_drawdown": 15.67,
    "total_trades": 23,
    "winning_trades": 15,
    "losing_trades": 8,
    "win_rate": 65.22,
    "avg_trade": 1966.54
  },
  "chart_data": {
    "dates": ["2020-01-02", "2020-01-03", ...],
    "prices": [75.09, 74.36, ...],
    "portfolio_values": [100000, 99850, ...],
    "trades": [
      {
        "date": "2020-01-15",
        "type": "BUY",
        "price": 77.12,
        "size": 1231,
        "value": 94956.72,
        "commission": 94.96
      },
      ...
    ]
  }
}
```

**Error (400/500):**

```json
{
  "error": "Error message describing what went wrong"
}
```

#### Response Fields

**Portfolio Object:**
- `starting_value`: Initial capital
- `ending_value`: Final portfolio value
- `total_return`: Profit/loss in dollars
- `total_return_pct`: Profit/loss percentage

**Metrics Object:**
- `sharpe_ratio`: Risk-adjusted returns (higher = better)
- `max_drawdown`: Maximum peak-to-trough decline
- `total_trades`: Number of completed buy-sell cycles
- `winning_trades`: Number of profitable trades
- `losing_trades`: Number of losing trades
- `win_rate`: Percentage of winning trades
- `avg_trade`: Average profit/loss per trade

**Chart Data Object:**
- `dates`: Array of date strings
- `prices`: Array of stock prices
- `portfolio_values`: Array of portfolio values
- `trades`: Array of trade objects

**Trade Object:**
- `date`: Trade execution date
- `type`: "BUY" or "SELL"
- `price`: Execution price
- `size`: Number of shares
- `value`: Total transaction value
- `commission`: Commission paid

---

## Custom Strategy Parameters

When using `strategy: "custom"`, include custom parameters:

```json
{
  "strategy": "custom",
  "custom_params": {
    "indicator": "SMA",
    "period1": 10,
    "period2": 30
  }
}
```

**Custom Parameters:**
- `indicator`: "SMA", "EMA", or "RSI"
- `period1`: Short period (or RSI period)
- `period2`: Long period (or RSI oversold level)

---

## Error Handling

Common error codes and meanings:

| Code | Meaning | Common Causes |
|------|---------|---------------|
| 400 | Bad Request | Invalid ticker, invalid dates, missing parameters |
| 500 | Server Error | Backend error, data fetch failure, strategy error |

**Error Response Example:**

```json
{
  "error": "No data found for ticker INVALID. Please check if the ticker symbol is correct."
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production use, consider:
- Implementing request throttling
- Caching frequent queries
- Using API keys for authentication

---

## Integration Examples

### Python

```python
import requests

response = requests.post('http://localhost:5000/api/backtest', json={
    'ticker': 'AAPL',
    'start_date': '2020-01-01',
    'end_date': '2023-01-01',
    'strategy': 'sma-crossover',
    'initial_cash': 100000,
    'commission': 0.001
})

data = response.json()
print(f"Total Return: ${data['portfolio']['total_return']:.2f}")
```

### JavaScript

```javascript
fetch('http://localhost:5000/api/backtest', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    ticker: 'AAPL',
    start_date: '2020-01-01',
    end_date: '2023-01-01',
    strategy: 'sma-crossover',
    initial_cash: 100000,
    commission: 0.001
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

### cURL

```bash
curl -X POST http://localhost:5000/api/backtest \
  -H "Content-Type: application/json" \
  -d @request.json
```

---

## CORS

CORS is enabled for all origins. For production, configure allowed origins in `app.py`:

```python
CORS(app, origins=['https://yourdomain.com'])
```

---

## Future API Endpoints (Roadmap)

- `GET /api/strategies` - List all available strategies
- `GET /api/tickers` - Search for valid tickers
- `POST /api/optimize` - Parameter optimization
- `GET /api/history` - Get previous backtests
- `POST /api/compare` - Compare multiple strategies

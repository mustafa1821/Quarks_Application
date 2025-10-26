"""
Quarks Backtesting PRO - Enhanced with Trade Tracking
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import backtrader as bt
import yfinance as yf
import pandas as pd
from datetime import datetime

app = Flask(__name__, static_folder='.')
CORS(app)

# Global trade tracker
trade_history = []

# ==================== BASE STRATEGY WITH TRACKING ====================

class BaseStrategy(bt.Strategy):
    """Base strategy with trade tracking"""
    
    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                trade_history.append({
                    'date': self.data.datetime.date(0).isoformat(),
                    'type': 'BUY',
                    'price': order.executed.price,
                    'size': order.executed.size,
                    'value': order.executed.value,
                    'commission': order.executed.comm
                })
            elif order.issell():
                trade_history.append({
                    'date': self.data.datetime.date(0).isoformat(),
                    'type': 'SELL',
                    'price': order.executed.price,
                    'size': order.executed.size,
                    'value': order.executed.value,
                    'commission': order.executed.comm
                })

# ==================== STRATEGY CLASSES ====================

class SMAStrategy(BaseStrategy):
    params = (('short_period', 10), ('long_period', 30))
    
    def __init__(self):
        self.sma_short = bt.indicators.SMA(self.data.close, period=self.params.short_period)
        self.sma_long = bt.indicators.SMA(self.data.close, period=self.params.long_period)
        self.crossover = bt.indicators.CrossOver(self.sma_short, self.sma_long)
    
    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.sell()

class EMAStrategy(BaseStrategy):
    params = (('short_period', 9), ('long_period', 21))
    
    def __init__(self):
        self.ema_short = bt.indicators.EMA(self.data.close, period=self.params.short_period)
        self.ema_long = bt.indicators.EMA(self.data.close, period=self.params.long_period)
        self.crossover = bt.indicators.CrossOver(self.ema_short, self.ema_long)
    
    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.sell()

class RSIStrategy(BaseStrategy):
    params = (('period', 14), ('oversold', 30), ('overbought', 70))
    
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close, period=self.params.period)
    
    def next(self):
        if not self.position:
            if self.rsi < self.params.oversold:
                self.buy()
        elif self.rsi > self.params.overbought:
            self.sell()

class MACDStrategy(BaseStrategy):
    params = (('fast', 12), ('slow', 26), ('signal', 9))
    
    def __init__(self):
        self.macd = bt.indicators.MACD(self.data.close, period_me1=self.params.fast,
                                       period_me2=self.params.slow, period_signal=self.params.signal)
    
    def next(self):
        if not self.position:
            if self.macd.macd > self.macd.signal:
                self.buy()
        elif self.macd.macd < self.macd.signal:
            self.sell()

class BollingerBandsStrategy(BaseStrategy):
    params = (('period', 20), ('devfactor', 2))
    
    def __init__(self):
        self.bbands = bt.indicators.BollingerBands(self.data.close, period=self.params.period,
                                                     devfactor=self.params.devfactor)
    
    def next(self):
        if not self.position:
            if self.data.close < self.bbands.lines.bot:
                self.buy()
        elif self.data.close > self.bbands.lines.top:
            self.sell()

class StochasticStrategy(BaseStrategy):
    params = (('period', 14), ('period_dfast', 3), ('oversold', 20), ('overbought', 80))
    
    def __init__(self):
        self.stochastic = bt.indicators.Stochastic(self.data, period=self.params.period,
                                                    period_dfast=self.params.period_dfast)
    
    def next(self):
        if not self.position:
            if self.stochastic.percK < self.params.oversold:
                self.buy()
        elif self.stochastic.percK > self.params.overbought:
            self.sell()

class MomentumStrategy(BaseStrategy):
    params = (('period', 10),)
    
    def __init__(self):
        self.momentum = bt.indicators.Momentum(self.data.close, period=self.params.period)
    
    def next(self):
        if not self.position:
            if self.momentum > 0:
                self.buy()
        elif self.momentum < 0:
            self.sell()

class TripleSMAStrategy(BaseStrategy):
    params = (('short', 5), ('medium', 15), ('long', 30))
    
    def __init__(self):
        self.sma_short = bt.indicators.SMA(self.data.close, period=self.params.short)
        self.sma_medium = bt.indicators.SMA(self.data.close, period=self.params.medium)
        self.sma_long = bt.indicators.SMA(self.data.close, period=self.params.long)
    
    def next(self):
        if not self.position:
            if self.sma_short > self.sma_medium > self.sma_long:
                self.buy()
        elif self.sma_short < self.sma_medium:
            self.sell()

class MeanReversionStrategy(BaseStrategy):
    params = (('period', 20), ('threshold', 2))
    
    def __init__(self):
        self.sma = bt.indicators.SMA(self.data.close, period=self.params.period)
        self.stddev = bt.indicators.StdDev(self.data.close, period=self.params.period)
    
    def next(self):
        if self.stddev[0] != 0:
            deviation = (self.data.close[0] - self.sma[0]) / self.stddev[0]
            if not self.position:
                if deviation < -self.params.threshold:
                    self.buy()
            elif deviation > self.params.threshold:
                self.sell()

class BuyAndHoldStrategy(BaseStrategy):
    def __init__(self):
        self.order = None
    
    def next(self):
        if not self.position and self.order is None:
            self.order = self.buy()

class CustomStrategy(BaseStrategy):
    params = (('indicator', 'SMA'), ('period1', 10), ('period2', 30))
    
    def __init__(self):
        if self.params.indicator == 'SMA':
            self.ind1 = bt.indicators.SMA(self.data.close, period=self.params.period1)
            self.ind2 = bt.indicators.SMA(self.data.close, period=self.params.period2)
            self.crossover = bt.indicators.CrossOver(self.ind1, self.ind2)
        elif self.params.indicator == 'EMA':
            self.ind1 = bt.indicators.EMA(self.data.close, period=self.params.period1)
            self.ind2 = bt.indicators.EMA(self.data.close, period=self.params.period2)
            self.crossover = bt.indicators.CrossOver(self.ind1, self.ind2)
        elif self.params.indicator == 'RSI':
            self.ind1 = bt.indicators.RSI(self.data.close, period=self.params.period1)
    
    def next(self):
        if self.params.indicator in ['SMA', 'EMA']:
            if not self.position:
                if self.crossover > 0:
                    self.buy()
            elif self.crossover < 0:
                self.sell()
        elif self.params.indicator == 'RSI':
            if not self.position:
                if self.ind1 < self.params.period2:
                    self.buy()
            elif self.ind1 > 70:
                self.sell()

# ==================== POSITION SIZERS ====================

class PercentSizer(bt.Sizer):
    params = (('percent', 95),)
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            return int((cash * (self.params.percent / 100)) / data.close[0])
        return self.broker.getposition(data).size

class AllInSizer(bt.Sizer):
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            return int(cash / data.close[0])
        return self.broker.getposition(data).size

class FixedAmountSizer(bt.Sizer):
    params = (('amount', 10000),)
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            return int(min(self.params.amount, cash) / data.close[0])
        return self.broker.getposition(data).size

class FixedSharesSizer(bt.Sizer):
    params = (('shares', 100),)
    def _getsizing(self, comminfo, cash, data, isbuy):
        if isbuy:
            return self.params.shares if self.params.shares * data.close[0] <= cash else 0
        return self.broker.getposition(data).size

# ==================== MAPPINGS ====================

STRATEGIES = {
    'sma-crossover': SMAStrategy, 'ema-crossover': EMAStrategy, 'rsi': RSIStrategy,
    'macd': MACDStrategy, 'bollinger': BollingerBandsStrategy, 'stochastic': StochasticStrategy,
    'momentum': MomentumStrategy, 'triple-sma': TripleSMAStrategy,
    'mean-reversion': MeanReversionStrategy, 'buy-hold': BuyAndHoldStrategy, 'custom': CustomStrategy
}

# ==================== API ROUTES ====================

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/backtest', methods=['POST'])
def run_backtest():
    global trade_history
    trade_history = []  # Reset trade history
    
    try:
        data = request.json
        ticker = str(data.get('ticker', 'AAPL')).strip().upper()
        start_date = data.get('start_date', '2020-01-01')
        end_date = data.get('end_date', '2023-01-01')
        strategy_id = data.get('strategy', 'sma-crossover')
        initial_cash = float(data.get('initial_cash', 100000))
        commission = float(data.get('commission', 0.001))
        position_sizing = data.get('position_sizing', 'percent')
        position_value = float(data.get('position_value', 95))
        custom_params = data.get('custom_params', {})
        
        print(f"Downloading data for {ticker}...")
        stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        if isinstance(stock_data.columns, pd.MultiIndex):
            stock_data.columns = stock_data.columns.get_level_values(0)
        
        if stock_data.empty:
            return jsonify({'error': f'No data found for {ticker}'}), 400
        
        cerebro = bt.Cerebro()
        cerebro.adddata(bt.feeds.PandasData(dataname=stock_data))
        
        strategy_class = STRATEGIES.get(strategy_id, SMAStrategy)
        if strategy_id == 'custom' and custom_params:
            cerebro.addstrategy(strategy_class, **custom_params)
        else:
            cerebro.addstrategy(strategy_class)
        
        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=commission)
        
        if position_sizing == 'percent':
            cerebro.addsizer(PercentSizer, percent=position_value)
        elif position_sizing == 'all-in':
            cerebro.addsizer(AllInSizer)
        elif position_sizing == 'fixed-amount':
            cerebro.addsizer(FixedAmountSizer, amount=position_value)
        elif position_sizing == 'fixed-shares':
            cerebro.addsizer(FixedSharesSizer, shares=int(position_value))
        
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe', riskfreerate=0.01)
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
        
        print("Running backtest...")
        initial_value = cerebro.broker.getvalue()
        results = cerebro.run()
        final_value = cerebro.broker.getvalue()
        
        strat = results[0]
        sharpe = strat.analyzers.sharpe.get_analysis()
        drawdown = strat.analyzers.drawdown.get_analysis()
        trades = strat.analyzers.trades.get_analysis()
        
        total_return = final_value - initial_value
        total_return_pct = (total_return / initial_value) * 100
        sharpe_ratio = sharpe.get('sharperatio', 0) if sharpe.get('sharperatio') is not None else 0
        max_drawdown = drawdown.max.drawdown if hasattr(drawdown, 'max') else 0
        total_trades = trades.total.closed if hasattr(trades, 'total') else 0
        won_trades = trades.won.total if hasattr(trades, 'won') else 0
        lost_trades = trades.lost.total if hasattr(trades, 'lost') else 0
        win_rate = (won_trades / total_trades * 100) if total_trades > 0 else 0
        
        avg_trade = 0
        if hasattr(trades, 'won') and hasattr(trades.won, 'pnl'):
            won_pnl = trades.won.pnl.total if hasattr(trades.won.pnl, 'total') else 0
            lost_pnl = trades.lost.pnl.total if hasattr(trades, 'lost') and hasattr(trades.lost.pnl, 'total') else 0
            avg_trade = (won_pnl + lost_pnl) / total_trades if total_trades > 0 else 0
        
        # Calculate portfolio values over time
        portfolio_values = []
        current_cash = initial_cash
        current_shares = 0
        trade_idx = 0
        
        for i, date in enumerate(stock_data.index):
            date_str = date.strftime('%Y-%m-%d')
            price = stock_data['Close'].iloc[i]
            
            # Update cash and shares based on trades
            while trade_idx < len(trade_history) and trade_history[trade_idx]['date'] == date_str:
                trade = trade_history[trade_idx]
                if trade['type'] == 'BUY':
                    current_shares += trade['size']
                    current_cash -= trade['value'] + trade['commission']
                else:  # SELL
                    current_shares -= trade['size']
                    current_cash += trade['value'] - trade['commission']
                trade_idx += 1
            
            portfolio_value = current_cash + (current_shares * price)
            portfolio_values.append(portfolio_value)
        
        result = {
            'success': True,
            'portfolio': {
                'starting_value': initial_value, 'ending_value': final_value,
                'total_return': total_return, 'total_return_pct': total_return_pct
            },
            'metrics': {
                'sharpe_ratio': sharpe_ratio, 'max_drawdown': max_drawdown,
                'total_trades': total_trades, 'winning_trades': won_trades,
                'losing_trades': lost_trades, 'win_rate': win_rate, 'avg_trade': avg_trade
            },
            'chart_data': {
                'dates': [d.strftime('%Y-%m-%d') for d in stock_data.index],
                'prices': stock_data['Close'].tolist(),
                'portfolio_values': portfolio_values,
                'trades': trade_history
            }
        }
        
        print("Backtest completed!")
        return jsonify(result)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Quarks Backtesting PRO Server...")
    print("📊 11 Strategies Available (10 + Custom Builder)")
    print("📈 Enhanced Charts with Buy/Sell Markers")
    print("🔍 Zoom & Pan Enabled")
    print("🌐 Open http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

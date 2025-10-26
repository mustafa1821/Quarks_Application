# Contributing to Quarks Backtester

First off, thank you for considering contributing to Quarks! It's people like you that make Quarks such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and explain which behavior you expected to see instead**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python style guide (PEP 8)
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## Development Process

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** and test them thoroughly
3. **Update documentation** if you've changed functionality
4. **Write or adapt tests** as needed
5. **Ensure the test suite passes**
6. **Make sure your code lints** (PEP 8)
7. **Issue that pull request!**

### Setting Up Your Development Environment

```bash
# Clone your fork
git clone https://github.com/yourusername/quarks-backtester.git
cd quarks-backtester

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Coding Standards

* Follow PEP 8 style guide for Python code
* Use meaningful variable and function names
* Comment your code where necessary
* Keep functions small and focused
* Write docstrings for functions and classes

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Example:
```
Add RSI strategy parameter customization

- Allow users to set RSI period
- Add oversold/overbought level controls
- Update documentation

Fixes #123
```

## Project Structure

```
quarks-backtester/
├── app.py              # Flask backend with strategies
├── index.html          # Frontend interface
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── CONTRIBUTING.md    # This file
├── LICENSE            # MIT License
└── docs/              # Additional documentation
```

## Adding New Strategies

To add a new trading strategy:

1. Create a strategy class in `app.py` that inherits from `BaseStrategy`:

```python
class MyStrategy(BaseStrategy):
    params = (('period', 14),)
    
    def __init__(self):
        self.indicator = bt.indicators.SomeIndicator(period=self.params.period)
    
    def next(self):
        if not self.position:
            if condition_to_buy:
                self.buy()
        elif condition_to_sell:
            self.sell()
```

2. Add it to the `STRATEGIES` dictionary:

```python
STRATEGIES = {
    'my-strategy': MyStrategy,
    # ... other strategies
}
```

3. Add the option to the dropdown in `index.html`:

```html
<option value="my-strategy">My Strategy Name</option>
```

4. Test it thoroughly with various stocks and date ranges

5. Document the strategy in the README

## Testing

Before submitting a pull request:

1. Test with multiple tickers (AAPL, MSFT, TSLA, etc.)
2. Test with different date ranges
3. Test all position sizing methods
4. Test the custom strategy builder
5. Check the interactive chart features
6. Test on different browsers (Chrome, Firefox, Safari)
7. Test on mobile devices if possible

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## Thank You!

Your contributions to open source, large or small, make projects like this possible. Thank you for taking the time to contribute.

# Ediscoins Strategy: Advanced Cryptocurrency Trading Algorithm

## Introduction

Welcome to Ediscoins, a sophisticated algorithmic trading strategy for cryptocurrency markets. This strategy represents the culmination of two years of intensive research and development, inspired by Thomas Edison's relentless pursuit of innovation.

## Background

- **Two Years of Research**: Like Edison's 1,000 attempts to create the light bulb, Ediscoins is the result of tireless experimentation in crypto trading.
- **Continuous Optimization**: Each of the 25 parameters per trading pair undergoes constant hyperoptimization using a one-year rolling window.
- **Computational Power**: The optimization process harnesses power equivalent to 20 Apple M3 Pro Max chips, ensuring cutting-edge performance.

## Key Features

- Optimized for 5-minute timeframes
- Currently tailored for Binance exchange
- Individually optimized trading pairs
- High win rate in live trading (often exceeding 80%)
- Adaptive to various market conditions
- Focused on spot trading and long positions only

## Setup Instructions

1. **Environment**: 
   - Requires Python 3.12
   - Compatible with Windows, macOS, and Linux

2. **File Placement**:
   - Place `EdisCoins_obf.py` and `EdisCoins.py` in your Freqtrade `strategies` folder (freqtrade/user_data
/strategies)
   - Ensure `pyarmor_runtime_006349` folder is in the `strategies` folder
   - Put `pair_params.py` in the Freqtrade root folder

3. **Configuration**:
   - Use `EdisCoins` as the strategy name when running Freqtrade
   - Example: `freqtrade trade -s EdisCoins`

## Strategy Configuration (config.json)

- `max_open_trades`: 3 to 5 (adjust based on risk appetite)
- `stake_currency`: USDT
- `timeframe`: 5m (mandatory)
- `exchange`: Binance
- `pairlists`: Use `StaticPairList`
- Include all pairs from the provided whitelist
- Maintain the provided blacklist

## Important Notes

- This is an MVP (Minimum Viable Product) release
- Strategy will expire on October 24, 2024 (no buy signals after this date)
- A full version with ongoing updates will be available on ediscoins.io

## Performance

Ediscoins has demonstrated exceptional performance in live trading:
- Consistent profitability across multiple weeks
- High win rate
- Effective risk management

## Strategy Robustness

Ediscoins has been meticulously designed to avoid common pitfalls in algorithmic trading:

- **Backtesting Traps**: Our strategy accounts for issues like trade timeouts, slippage, and unrealistic trailing stop behavior in longer timeframes.
- **Lookahead Bias**: We've carefully structured our code to prevent accidentally "seeing into the future" during backtesting and live trading.
- **Realistic Performance**: Our results consider factors like spread, unfilled orders, and market dynamics, providing a more accurate representation of live trading performance.
- **Time-Appropriate Signals**: The strategy uses a 5-minute timeframe for execution while leveraging 1-hour informative timeframes for signal generation, ensuring more realistic backtesting results.
- **Spot Trading Focus**: Ediscoins is designed specifically for spot trading, focusing exclusively on long positions to capitalize on market uptrends.

These considerations contribute to the strategy's robust performance in live trading conditions.

## Future Development

A subscription-based version with continuously updated parameters will be available soon on ediscoins.io.

## Disclaimer

Cryptocurrency trading involves significant risk. This strategy, while optimized and tested, does not guarantee profits. Always trade responsibly and within your means.

## License

This strategy is provided under [EdisCoins License Terms]. See the LICENSE file for more details.

---

For more information, updates, and support, visit [ediscoins.io](https://ediscoins.io).

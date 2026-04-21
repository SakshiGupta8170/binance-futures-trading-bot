# Binance Futures Trading Bot

This project places MARKET and LIMIT orders on Binance Futures Testnet.

## Setup
pip install -r requirements.txt

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

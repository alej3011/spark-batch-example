# Vamos a crear un productor de datos de Google Finance

from kafka import KafkaProducer
import yfinance as yf
import json
import time

TICKERS = ['GOOG', '^GSPC']
TOPIC = 'financial_data'

producer = KafkaProducer(
    bootstrap_servers="localhost:9092", 
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    for ticker in TICKERS:
        data = yf.Ticker(ticker).history(period="1d", interval="1m").tail(1)
        if not data.empty:
            row = data.iloc[0]
            print(row)
            producer.send(
                TOPIC,
                {
                    'symbol': ticker,
                    'open': float(row['Open']),
                    'close': float(row['Close']),
                    'high': float(row['High']),
                    'low': float(row['Low']),
                    'volume': int(row['Volume']),
                }
            )
            print(f"Sent financial data for {ticker}")
    time.sleep(5)

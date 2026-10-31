
import pandas as pd
import numpy as np

df = pd.read_csv('BTCUSDT-1m-2026-07.csv')

# час відкриття свічки: мікросекунди -> UTC
df['open_time'] = pd.to_datetime(df['open_time'], unit='us', utc=True)

# лог дохідність close-to-close: ln(close_t / close_{t-1})
df['log_return'] = np.log(df['close'] / df['close'].shift(1))

# перша свічка без попереднього закриття -> NaN, викидаємо
out = df[['open_time', 'log_return']].dropna()

out.to_csv('BTCUSDT-1m-2026-07-returns.csv', index=False)



import pandas as pd

def unpivot_data(row):
  """Transforms raw data into a DataFrame with un pivoted structure."""

  rows = []
  success = row['success']
  timestamp = row['timestamp']
  historical = row['historical']
  base = row['base']
  date = row['date']
  rates = row['rates']

  for currency_code, exchange_rate in rates.items():
    rows.append([success, timestamp, historical, base, date, currency_code, exchange_rate])

  return pd.DataFrame(rows, columns=['success', 'timestamp', 'historical', 'base', 'date', 'currency_code', 'exchange_rate'])

def transform_data(exchange_rates):
  """Applies unpivoting transformation to the list of exchange rate data."""

  df = pd.DataFrame(exchange_rates)
  result_df = df.apply(lambda row: unpivot_data(row), axis=1)
  final_df = pd.concat(result_df.tolist(), ignore_index=True)
  final_df = final_df.drop(['historical', 'success'], axis=1)
  final_df['rate_id'] = range(1, len(final_df) + 1)

  return final_df

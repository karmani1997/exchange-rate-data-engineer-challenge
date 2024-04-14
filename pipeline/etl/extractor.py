import requests
from datetime import timedelta

def fetch_exchange_rates(API_KEY, base_currency, target_currencies, start_date, end_date):
  """Fetches exchange rates data from external API."""

  rates_data = []
  current_date = start_date

  while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    api_url = f"http://api.exchangeratesapi.io/v1/{date_str}?access_key={API_KEY}&base={base_currency}&symbols={','.join(target_currencies)}"
    response = requests.get(api_url)
    data = response.json()
    rates_data.append(data)
    current_date += timedelta(days=1)

  return rates_data

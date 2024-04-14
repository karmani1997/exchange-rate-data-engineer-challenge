import os
import extractor
import transformer as transformer
import loader
# Load configuration from config.py
from config import API_KEY, TABLE_ID, BASE_CURRENCY, TARGET_CURRENCIES, START_DATE, END_DATE, CREDENTIALS_PATH


# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH

if __name__ == '__main__':

    # Extract data
    exchange_rates = extractor.fetch_exchange_rates(API_KEY, BASE_CURRENCY, TARGET_CURRENCIES, START_DATE, END_DATE)

    # Transform data
    df = transformer.transform_data(exchange_rates)

    # Load data
    loader.store_data_in_bigquery(df, TABLE_ID)

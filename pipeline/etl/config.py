from datetime import datetime, timedelta

API_KEY = '####'
PROJECT_ID = 'PROJECT_ID'  # Assuming you have a project ID
DATASET_ID = 'DATASET_ID'
TABLE_ID = f"{PROJECT_ID}.{DATASET_ID}.currency_rates"  # Construct the full table ID
BASE_CURRENCY = 'EUR'
TARGET_CURRENCIES = ['USD', 'GBP', 'CHF']
START_DATE = datetime.now() - timedelta(days=90)
END_DATE = datetime.now()
CREDENTIALS_PATH = 'credential.json'
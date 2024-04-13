
from google.cloud import bigquery

def currencyrates_table_schema():
    return [
        bigquery.SchemaField("rate_id", "INTEGER", mode="REQUIRED", description="Unique identifier for each rate entry"),
        bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED", description="Timestamp of the rate entry"),
        bigquery.SchemaField("base", "STRING", mode="REQUIRED", description="The base currency"),
        bigquery.SchemaField("date", "STRING", mode="REQUIRED", description="The date of the rates"),
        bigquery.SchemaField("currency_code", "STRING", mode="REQUIRED", description="The code of the currency (e.g., USD, GBP, CHF)"),
        bigquery.SchemaField("exchange_rate", "FLOAT", mode="REQUIRED", description="The exchange rate for the respective currency on the given date"),
    ]

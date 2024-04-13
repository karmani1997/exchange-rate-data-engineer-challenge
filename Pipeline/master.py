import requests
import pandas as pd
import os
from datetime import datetime, timedelta
from google.cloud import bigquery

# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../river-daylight-420211-523e5d1f8610.json'

# Construct a BigQuery client object.
client = bigquery.Client()


##Extract data
def fetch_exchange_rates(API_KEY, base_currency, target_currencies, start_date, end_date):

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

##Transform data
# Define the unpivot_data function
def unpivot_data(row):
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


##Load data
def store_data_in_bigquery(data):
    client = bigquery.Client()
    project_id = 'river-daylight-420211'
    dataset_id = 'exchange_rate_dataset'
    table_id = 'currencyrates'

    job_config = bigquery.LoadJobConfig(
    # Specify a (partial) schema. All columns are always written to the
    # table. The schema is used to assist in data type definitions.
    schema = [
        bigquery.SchemaField("rate_id", "INTEGER", mode="REQUIRED", description="Unique identifier for each rate entry"),
        bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED", description="Timestamp of the rate entry"),
        bigquery.SchemaField("base", "STRING", mode="REQUIRED", description="The base currency"),
        bigquery.SchemaField("date", "STRING", mode="REQUIRED", description="The date of the rates"),
        bigquery.SchemaField("currency_code", "STRING", mode="REQUIRED", description="The code of the currency (e.g., USD, GBP, CHF)"),
        bigquery.SchemaField("exchange_rate", "FLOAT", mode="REQUIRED", description="The exchange rate for the respective currency on the given date"),
    ]
    # Optionally, set the write disposition. BigQuery appends loaded rows
    # to an existing table by default, but with WRITE_TRUNCATE write
    # disposition it replaces the table with the loaded data.
    #write_disposition="WRITE_TRUNCATE",
    )
    
    table_ref = client.dataset(dataset_id,project=project_id).table(table_id)
    # table = client.get_table(table_ref)
    table_id = 'river-daylight-420211.exchange_rate_dataset.currencyrates'
    # errors = client.insert_rows_json(table, data)
    # if errors:
    #     print("Errors occurred while inserting rows: {}".format(errors))
    job = client.load_table_from_dataframe(data, table_id , job_config=job_config)  # Make an API request.
    job.result()  # Wait for the job to complete.

    table = client.get_table(table_id)  # Make an API request.
    print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
    )

if __name__ == '__main__':

    ##load
    API_KEY = '0fd5492ce37b5afa389fd204e9fb854c'
    base_currency = 'EUR'
    target_currencies = ['USD', 'GBP', 'CHF']
    #end_date = datetime.now().strftime('%Y-%m-%d')
    #start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')  # 3 months back
    start_date = datetime.now() - timedelta(days=1)
    end_date = datetime.now()
    exchange_rates = fetch_exchange_rates(API_KEY, base_currency, target_currencies, start_date, end_date)

    ## transfrom
    df = pd.DataFrame(exchange_rates)
    # Apply the function to the DataFrame using lambda
    result_df = df.apply(lambda row: unpivot_data(row), axis=1)
    # Concatenate the resulting DataFrames into one
    final_df = pd.concat(result_df.tolist(), ignore_index=True)
    final_df = final_df.drop(['historical', 'success'], axis=1)
    final_df['rate_id'] = range(1, len(final_df) + 1)
    
    ##Load 
    store_data_in_bigquery(final_df)
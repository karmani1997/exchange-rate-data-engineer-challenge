import model
from google.cloud import bigquery

def store_data_in_bigquery(data, table_id):
  """Loads the transformed data into BigQuery."""

  client = bigquery.Client()
  job_config = bigquery.LoadJobConfig(schema = model.currencyrates_table_schema())

  job = client.load_table_from_dataframe(data, table_id, job_config=job_config)
  
  job.result()

  table = client.get_table(table_id)
  print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")


# Task 1
## Exchange Rate Data Processing

This project is aimed at extracting exchange rate data from an external API, transforming it into a suitable format, and loading it into a BigQuery table.

### Modules

#### extractor.py

This module contains the functionality to extract exchange rate data from an external API using the provided API key, base currency, target currencies, start date, and end date.

##### Function:
- `fetch_exchange_rates(API_KEY, base_currency, target_currencies, start_date, end_date)`: Fetches exchange rate data from the API for the specified parameters.

#### transformer.py

This module contains the functionality to transform the raw exchange rate data into a format suitable for loading into a BigQuery table.

##### Function:
- `unpivot_data(row)`: Transforms the raw exchange rate data into a DataFrame with columns: success, timestamp, historical, base, date, currency_code, exchange_rate.

#### loader.py

This module contains the functionality to load the transformed exchange rate data into a BigQuery table.

##### Function:
- `store_data_in_bigquery(data)`: Loads the transformed exchange rate data into the specified BigQuery table.

#### model.py

This module contains the schema definition for the BigQuery table.

##### Function:
- `get_table_schema()`: Returns the schema for the BigQuery table.

### Usage

1. Make sure you have set up Google Cloud credentials and installed the required libraries specified in `requirements.txt`.
2. Modify `main.py` to specify the API key, base currency, target currencies, and date range for the exchange rate data you want to extract.
3. Run `main.py` to execute the data processing pipeline.

## Table Definition
Table(currencyrates) Definition for BigQuery:

| Field Name     | Type      | Mode      | Description                                                                    |
|----------------|-----------|-----------|--------------------------------------------------------------------------------|
| rate_id        | INTEGER   | REQUIRED  | Unique identifier for each rate entry.                                         |
| timestamp      | TIMESTAMP | REQUIRED  | Timestamp of the rate entry.                                                    |
| base           | STRING    | REQUIRED  | The base currency.                                                              |
| date           | STRING    | REQUIRED  | The date of the rates.                                                          |
| currency_code  | STRING    | REQUIRED  | The code of the currency (e.g., USD, GBP, CHF).                                |
| exchange_rate  | FLOAT     | REQUIRED  | The exchange rate for the respective currency on the given date.               |

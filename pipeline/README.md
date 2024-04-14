# Task 1
## Overview
This ETL pipeline automates the extraction, transformation, and loading (ETL) process of last 3 month exchange rate data into a Data Warehouse (DWH). The pipeline is implemented using Python.

## Folder Structure

- **etl/extractor.py:** This module contains the functionality to extract exchange rate data from an external API using the provided API key, base currency, target currencies, start date, and end date.
- **etl/transformer.py:** This module contains the functionality to transform the raw exchange rate data into a format suitable for loading into a BigQuery table.
- **etl/loader.py:** This module contains the functionality to load the transformed exchange rate data into a BigQuery table.
- **etl/model.py:** This module contains the schema definition for the BigQuery table.


### Usage

1. Make sure you have Google Service Account credentials stored in a JSON file placed in the etl folder, and that you have installed the required libraries specified in `requirements.txt`.
2. Modify `etl/config.py` to specify the API key, base currency, target currencies, Project_ID, Dataset_ID, Table_id and date range for the exchange rate data you want to extract.
3. Run `etl/main.py` to execute the data processing pipeline.

## Table Definition
Table(currency_rates) Definition for BigQuery:

| Field Name     | Type      | Mode      | Description                                                                    |
|----------------|-----------|-----------|--------------------------------------------------------------------------------|
| rate_id        | INTEGER   | REQUIRED  | Unique identifier for each rate entry.                                         |
| timestamp      | TIMESTAMP | REQUIRED  | Timestamp when the provided exchange rate information was collected.                                                    |
| base           | STRING    | REQUIRED  | The base currency code.                                                              |
| date           | STRING    | REQUIRED  | The date when the given exchange rate information was collected.                                                          |
| target_currency_code  | STRING    | REQUIRED  | The code of the target currency code (e.g., USD, GBP, CHF).                                |
| exchange_rate  | FLOAT     | REQUIRED  | The exchange rate for the respective currency on the given date.               |

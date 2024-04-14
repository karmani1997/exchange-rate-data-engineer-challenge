# Task 2: Data Architecture and Pipeline Design

## Data Pipeline Design:
![Pipeline Diagram](flow.png)

## Explanation for the stages

## Overview:
- This pipeline design follows an ETL (Extract, Load, Transform) approach, where data is first extracted, transformed and then loaded.
- Scheduling the data extraction ensures daily updates in BigQuery.

### The data pipeline will consist of the following stages:

### Data Extraction:

- This stage utilizes the script from Task 1 to fetch daily exchange rates from the external API ([Exchange Rates API](https://exchangeratesapi.io/)).
- The `extractor.py` module can be triggered daily using a scheduler like Cloud Scheduler or Airflow.
### Data Ingestion
- This stage stores the raw JSON files extracted by the extractor into data lake.
- The data is stored in a datewise folder structure.

### Data Transformation:
- The raw data retrieved from the API may require transformation before loading into data.
- This might involve cleaning, filtering, or reshaping the data.
- The `transformer.py` module can be used for this purpose.

### Data Validation:
- It's crucial to ensure data quality before loading.
- Implement data validation checks to identify missing values, invalid formats, or outliers.
- You can raise errors or log warnings for further investigation.

### Data Loading:

- The transformed and validated data is loaded into the BigQuery table defined in `model.py`.
- The `loader.py` module can handle this stage using BigQuery's load functionality.

### Data Partitioning:

- For better performance and manageability, consider partitioning the BigQuery table by date.
- This allows efficient querying for specific date ranges.
- You can configure table partitioning during table creation or implement logic to partition data after loading.

## Additional Considerations:
- Data validation is essential for maintaining data integrity.
- Partitioning the table by date optimizes queries and data management.


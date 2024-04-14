# Data Pipeline for Exchange Rate Processing

This repository contains the code for a `data pipeline` designed to process exchange rate data and details `Data Architecture and Pipeline Design`. The pipeline comprises several stages, including data extraction, transformation, and loading into a BigQuery table. Additionally, a schema for the BigQuery table is provided to maintain data integrity and optimize querying, data pipeline design and  explaination of the architecture.

## Task 1
Please refer [Task 1 README](https://github.com/karmani1997/exchange-rate-data-engineer-challenge/tree/main/pipeline) for details as to how to run the pipeline locally.

## Task 2
Please refer [Task 2 README](https://github.com/karmani1997/exchange-rate-data-engineer-challenge/tree/main/task-2) for details Data Architecture and Pipeline Design.

## Improvements in Task 1 and Task 2
#### Task 1
#### Data Validation:
- It's crucial to ensure data quality before loading.
- Implement data validation checks to identify missing values, invalid formats, or outliers.
- You can raise errors or log warnings for further investigation.

#### Data Partitioning:

- For better performance and manageability, consider partitioning the BigQuery table by date.
- This allows efficient querying for specific date ranges.
- You can configure table partitioning during table creation or implement logic to partition data after loading.
### Task 2
#### Error handling: 
- Implement mechanisms to handle potential errors during each stage (e.g., API failures, transformation errors, loading issues).

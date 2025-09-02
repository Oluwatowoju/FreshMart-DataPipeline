This project applies an ETL data pipeline for managing FreshMart's product data. The pipeline ingests raw CSV data, performs a transformation  with Pandas, and loads the cleaned data into a PostgreSQL database for storage and analysis.
DATA INGESTION:  Data was sourced from a CSV file containing product information, including Product ID, Product Name, Category, Price, and Stock Quantity.  Pandas  and the CSV library were used to achieve this.
DATA TRANSFORMATION: Pandas was utilised for cleaning and formatting,  removing duplicates, handling missing values, rounding numeric columns, as well as adding computed columns.
DATA STORAGE: The transformed data was loaded into a PostgreSQL database.
Database Connection: Psycopg2 was used to establish a connection to the PostgreSQL database.
DATABASE QUERY: SQL syntax was written to run the query to fetch my data.

Technologies used:
VS code
Pandas
Psycopg2
PostgreSQL
Jupyter Notebook

import csv
import psycopg2
import pandas as pd

# Database connection function
def get_db_connection():
    return psycopg2.connect (
        host ='localhost', 
        database = 'Fresh_Mart_db',
        user = 'postgres',
        password ='Tiwalade16',
        port = '5432'
    )
    return connection

conn = get_db_connection()
print("Connection succesful:", conn)

# create schema and table if not exists
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    create_table_query = '''
                            CREATE SCHEMA IF NOT EXISTS fresh_mart;

                            DROP TABLE IF EXISTS fresh_mart.products;

                            CREATE TABLE fresh_mart.products (
                                ProductID SERIAL PRIMARY KEY,
                                ProductName VARCHAR,
                                Category VARCHAR,
                                Price DECIMAL,
                                StockQuantity INT,
                                StockValue DECIMAL
                            );
                            '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

    # Data Load
def load_data_from(csv_path):
    conn=get_db_connection()
    cursor = conn.cursor()
    with open(csv_path,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
               INSERT INTO fresh_mart.products(ProductName, Category, Price, StockQuantity, StockValue)
               VALUES(%s, %s, %s, %s, %s)
            ''', (
                row['ProductName'],
                row['Category'],
                row['Price'],
                row['StockQuantity'],
                row['StockValue']
            ))
        conn.commit()
        cursor.close()
        conn.close()
        print("CSV data loaded successfully!")


csv_file_path = r'Dataset\CleanedData\products.csv'
load_data_from(csv_file_path)  
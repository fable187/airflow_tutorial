import cx_Oracle
import pandas as pd

# Connection details
dsn = cx_Oracle.makedsn("host", "port", service_name="service_name")
username = "username"
password = "password"

def insert_data_from_dataframe(table_name, dataframe):
    # Extract column names from the DataFrame's columns
    columns = list(dataframe.columns)

    # Generate the SQL statement based on the extracted columns
    insert_statement = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join([':' + str(i + 1) for i in range(len(columns))])})"

    # Connect to the database
    conn = cx_Oracle.connect(username, password, dsn)
    cursor = conn.cursor()

    # Prepare the statement
    cursor.prepare(insert_statement)

    # Extract values from the DataFrame and insert using prepared statement
    try:
        cursor.executemany(None, dataframe.values.tolist())
        conn.commit()
        print("Insertion successful")
    except cx_Oracle.Error as error:
        print("Error:", error)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Example usage:
# Create a sample DataFrame
data = {
    'column1': ['value1', 'value3', '

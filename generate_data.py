import sqlite3
import random
import string

def generate_random_data():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def create_sqlite_database(database_name, num_rows):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            data TEXT
        )
    ''')

    # Insert random data
    for _ in range(num_rows):
        data = generate_random_data()
        cursor.execute('INSERT INTO my_table (data) VALUES (?)', (data,))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    # Adjust the following variables to control the amount of data generated
    num_rows = 10000000  # Number of rows
    gigabytes = 1  # Target size in gigabytes

    # Calculate the size of each row (in bytes) to achieve the target size
    target_size_bytes = gigabytes * (1024 ** 3)
    average_row_size_bytes = target_size_bytes / num_rows

    # Generate SQLite database
    database_name = 'generated_data.db'
    create_sqlite_database(database_name, num_rows)

    print(f"SQLite database '{database_name}' generated successfully.")

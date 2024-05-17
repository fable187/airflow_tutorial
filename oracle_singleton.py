import oracledb

class OracleDBSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(OracleDBSingleton, cls).__new__(cls)
            cls._instance._init_db_connection(*args, **kwargs)
        return cls._instance

    def _init_db_connection(self, user, password, dsn):
        self.connection = oracledb.connect(user=user, password=password, dsn=dsn)
        self.cursor = self.connection.cursor()

    def _get_table_schema(self, table):
        sql = f"SELECT column_name FROM all_tab_columns WHERE table_name = :1"
        self.cursor.execute(sql, [table.upper()])
        columns = [row[0] for row in self.cursor.fetchall()]
        return columns

    def validate_schema(self, table, data):
        table_schema = self._get_table_schema(table)
        data_schema = data.keys()
        if set(table_schema) != set(data_schema):
            raise ValueError(f"Schema mismatch: Table schema is {table_schema}, but data schema is {data_schema}")

    def insert(self, table, data):
        self.validate_schema(table, data)
        keys = data.keys()
        columns = ', '.join(keys)
        placeholders = ', '.join([':' + str(i+1) for i in range(len(keys))])
        sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(sql, list(data.values()))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

# Example usage with context manager
if __name__ == "__main__":
    with OracleDBSingleton(user='your_username', password='your_password', dsn='your_dsn') as db:
        # Insert data
        data = {
            'COLUMN1': 'value1',
            'COLUMN2': 'value2',
            'COLUMN3': 'value3',
        }
        db.insert('YOUR_TABLE', data)

    # No need to explicitly close, as the context manager handles it

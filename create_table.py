import pandas as pd

def generate_create_table_sql(df, table_name):
    dtype_mapping = {
        'object': 'VARCHAR2(255)',
        'int64': 'NUMBER',
        'float64': 'FLOAT',
        'datetime64[ns]': 'DATE',
        'bool': 'NUMBER(1)'
    }

    columns = []
    for col_name, dtype in df.dtypes.iteritems():
        oracle_type = dtype_mapping.get(str(dtype), 'VARCHAR2(255)')
        columns.append(f"{col_name} {oracle_type}")
    columns_str = ", ".join(columns)
    create_table_sql = f"CREATE TABLE {table_name} ({columns_str})"
    
    return create_table_sql

# Example usage
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [70000.00, 80000.50, 90000.75],
    'is_manager': [False, True, True],
    'hire_date': pd.to_datetime(['2020-01-15', '2018-05-23', '2019-11-01'])
})

table_name = "employee"
create_table_sql = generate_create_table_sql(df, table_name)
print(create_table_sql)

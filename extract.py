import pandas as pd
from sqlalchemy import create_engine, inspect
from config import DB_CONNECTION_STRING

def get_engine():
    engine = create_engine(DB_CONNECTION_STRING)
    return engine.execution_options(schema_translate_map={None:"useranki140"})


TABLES=[
    "product_offering",
    "product_offering_price",
    "product_offering_characteristic",
    "product_offering_category",
    "category_master",
    "characteristic_master"
]
def get_table_columns(engine, table_name):
    inspector = inspect(engine)
    return [col["name"] for col in inspector.get_columns(table_name)]

def extract_table(engine, table_name):
    columns = get_table_columns(engine, table_name)
    column_list= ", ".join(columns)
    query=f"SELECT {column_list} FROM {table_name}"
    return pd.read_sql(query,engine)

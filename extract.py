import pandas as pd
from sqlalchemy import create_engine
from config import DB_CONNECTION_STRING

def get_engine():
    engine = create_engine(DB_CONNECTION_STRING)

def extract_product_offering(engine):
    query="SELECT id,description,unit_type,hsn_sac_code,valid_end_datetime FROM product_offering"
    return pd.read_sql(query,engine)

def extract_product_offering_price(engine):
    query="SELECT id, name, tax_schema_code from product_offering_price"
    return pd.read_sql(query,engine)

def extract_product_offering_characteristic(engine):
    query="SELECT id, product_offering_id,characteristic_code_id, characteristic_value from product_offering_characteristic"
    return pd.read_sql(query,engine)

def extract_product_offering_category(engine):
    query = "SELECT id, product_offering_id, category_master_id FROM product_offering_category"
    return pd.read_sql(query, engine)

def extract_category_master(engine):
    query="SELECT id, name FROM category_master"
    return pd.read_sql(query,engine)

def extract_characteristic_master(engine):
    query="SELECT characteristic_code, characteristic_name, characteristic_value_type FROM characteristic_master"
    return pd.read_sql(query,engine)


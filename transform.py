# transform.py
from mapping import (
    product_offering_mapping,
    product_offering_price_mapping,
    product_offering_characteristic_mapping,
    characteristic_master_mapping,
)

def rename_known(df, mapping):
    """Only rename columns that actually exist in this DataFrame."""
    valid = {k: v for k, v in mapping.items() if k in df.columns}
    return df.rename(columns=valid)


def build_product_sheet(df_offering, df_category, df_category_master):
    # Step A: resolve category_master_id -> the actual category name
    df_cat_joined = df_category.merge(
        df_category_master.rename(columns={"id": "category_master_id", "name": "category_name"}),
        on="category_master_id",
        how="left",
    )

    # Step B: attach the resolved category name onto the base product table
    df = df_offering.merge(
        df_cat_joined[["product_offering_id", "category_name"]],
        left_on="id",
        right_on="product_offering_id",
        how="left",
    )

    return rename_known(df, product_offering_mapping)


def build_price_sheet(df_price):
    return rename_known(df_price, product_offering_price_mapping)


def build_characteristics_sheet(df_char, df_char_master):
    df = df_char.merge(
        df_char_master.rename(columns={"characteristic_code": "characteristic_code"}),
        on="characteristic_code",
        how="left",
    )
    return rename_known(df, product_offering_characteristic_mapping)
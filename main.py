import pandas as pd

from extract import (
    get_engine,
    extract_category_master,
    extract_characteristic_master,
    extract_product_offering,
    extract_product_offering_category,
    extract_product_offering_characteristic,
    extract_product_offering_price
)
from transform import(
    build_characteristics_sheet,
    build_price_sheet,
    build_product_sheet
)

def strip_timezones(df):
    for col in df.columns:
        if pd.api.types.is_datetime64tz_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)
    return df

def main():
    engine = get_engine()

    # extracting raw tables
    df_offering = extract_product_offering(engine)
    df_price = extract_product_offering_price(engine)
    df_category = extract_product_offering_category(engine)
    df_category_master = extract_category_master(engine)
    df_char = extract_product_offering_characteristic(engine)
    df_char_master = extract_characteristic_master(engine)

    # transform into final report tables
    product_sheet = build_product_sheet(df_offering, df_category, df_category_master)
    price_sheet = build_price_sheet(df_price,df_offering)
    characteristics_sheet = build_characteristics_sheet(df_char, df_char_master)

    product_sheet = strip_timezones(product_sheet)
    price_sheet = strip_timezones(price_sheet)
    characteristics_sheet = strip_timezones(characteristics_sheet)
    # write to Excel — one file, three sheets
    with pd.ExcelWriter("product_report.xlsx", engine="openpyxl") as writer:
        product_sheet.to_excel(writer, sheet_name="Product", index=False)
        price_sheet.to_excel(writer, sheet_name="Price", index=False)
        characteristics_sheet.to_excel(writer, sheet_name="Custom", index=False)

    print("Report written to product_report.xlsx")


if __name__=="__main__":
    main()


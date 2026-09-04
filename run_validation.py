import pandas as pd

from validate import(
    validate_product_row,
    validate_price_row,
    validate_characteristics_row,
)

REPORT_FILE="product_report.xlsx"


def main():

    product_sheet=pd.read_excel(REPORT_FILE,sheet_name="Product")

    price_sheet=pd.read_excel(REPORT_FILE,sheet_name="Price")

    characteristics_sheet=pd.read_excel(REPORT_FILE,sheet_name="Custom") # for now Characteristics later replace to Custom

    # NaN to None 

    product_sheet=product_sheet.where(pd.notna(product_sheet),None)

    price_sheet=price_sheet.where(pd.notna(price_sheet),None)

    characteristics_sheet=characteristics_sheet.where(pd.notna(characteristics_sheet),None)


    # applying validation

    product_sheet["Error"]=product_sheet.apply(validate_product_row,axis=1)

    price_sheet["Error"]=price_sheet.apply(validate_price_row,axis=1)

    characteristics_sheet["Error"]=characteristics_sheet.apply(validate_characteristics_row,axis=1)

    with pd.ExcelWriter(REPORT_FILE,engine="openpyxl")as writer:
        product_sheet.to_excel(writer,sheet_name="Product",index=False)
        price_sheet.to_excel(writer,sheet_name="Price",index=False)
        characteristics_sheet.to_excel(writer,sheet_name="Custom",index=False)# for now Characteristics later replace to Custom
    print(f"Validation complete - {REPORT_FILE} Updated with error columns. ")

if __name__=="__main__":
    main()








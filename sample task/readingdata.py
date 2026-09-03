
import pandas as pd

reading_excel= pd.read_excel("sample_excel.xls")
print ("data retrived from excel",reading_excel)


print("end of excel")

reading_csv=pd.read_csv("samplecsv.csv",encoding="utf-8")

print("data retrived by csv",reading_csv)



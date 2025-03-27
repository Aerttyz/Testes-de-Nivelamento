import pdfplumber
import pandas as pd

pdf_path = "/content/pdfs/Anexo I..pdf"

with pdfplumber.open(pdf_path) as file:
  tables = []
  print(len(file.pages))
  for number_of_pages in file.pages:
    table = number_of_pages.extract_table()
    if table:
      tables.extend(table)

df = pd.DataFrame(tables[1:], columns=tables[0])

df.to_csv("saida.csv", index=False)
import pdfplumber
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scraping import compressor


pdf_path = "/content/pdfs/Anexo I..pdf"

with pdfplumber.open(pdf_path) as file:
  tables = []
  for number_of_pages in file.pages:
    table = number_of_pages.extract_table()
    if table:
      tables.extend(table)

df = pd.DataFrame(tables[1:], columns=tables[0])

df.rename(columns=lambda x: x.replace("OD", "Seg. Odontológica").replace("AMB", "Seg. Ambulatorial"), inplace=True) 

saida_csv_path = "/content/csv/saida.csv"
os.makedirs("/content/csv", exist_ok=True)
df.to_csv(saida_csv_path, index=False)

os.makedirs("/content/compact_files", exist_ok=True)
compressor.compact_files(saida_csv_path, "/content/compact_files/Teste_alesandro.zip")
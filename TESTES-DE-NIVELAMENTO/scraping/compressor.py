from zipfile import ZipFile
import os

# Criando diretório para armazenar os arquivos compactados
compact_dir= "/content/compact_files"
os.makedirs(compact_dir, exist_ok=True)

# Caminho do arquivo compactado
compact_file_path = os.path.join(compact_dir, "compact_files.zip")

# Diretório dos arquivos a serem compactados
pdf_path = "/content/pdfs"

with ZipFile(compact_file_path, 'w') as zip:
  for file_name in os.listdir(pdf_path):
    if file_name.endswith('.pdf'):
      file_path = os.path.join(pdf_path, file_name)
      zip.write(file_path, arcname=file_name)


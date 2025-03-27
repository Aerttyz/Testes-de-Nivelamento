from zipfile import ZipFile
import os


def compact_files(input_path, compact_file_path):
    with ZipFile(compact_file_path, 'w') as zip:
        for file_name in os.listdir(input_path):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(input_path, file_name)
                zip.write(file_path, arcname=file_name)
    print(f"Arquivos compactados em: {compact_file_path}")


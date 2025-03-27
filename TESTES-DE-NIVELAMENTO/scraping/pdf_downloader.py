import requests
import re
from bs4 import BeautifulSoup
import os
import compressor


pdf_path = "/content/pdfs"
os.makedirs(pdf_path, exist_ok=True)

def download_pdf(pdf_url, pdf_name):
  try:
    response = requests.get(pdf_url)
    response.raise_for_status()
    pdf_file = os.path.join(pdf_path, pdf_name+".pdf")
    with open(pdf_file, 'wb') as file:
      file.write(response.content)
    print(f"pdf salvo em: {pdf_file}")
  except requests.exceptions.RequestException as e:
    print(f"Erro ao baixar o PDF: {e}")
    return None


url =  "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

try:
    for link in soup.find_all('a', string=re.compile(r'Anexo I\.|Anexo II\.')):
        if link.get('href').endswith('.pdf'):
            pdf_url = link.get('href' )
            pdf_name = link.text.strip()
            download_pdf(pdf_url, pdf_name)
            print("download realizado")
except Exception as e:
    print(e)

compressor.compact_files(pdf_path, "/content/compact_files/compact_files.zip")
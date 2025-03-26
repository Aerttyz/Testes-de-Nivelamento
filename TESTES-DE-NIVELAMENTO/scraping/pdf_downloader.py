import requests
import re
from bs4 import BeautifulSoup



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
            print(pdf_url, pdf_name)
except Exception as e:
    print(e)

from bs4 import BeautifulSoup
import requests

url = ("https://www.diariopanorama.com/")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

valores = soup.find_all('h2')

print("¡NOTICIAS TITULARES DE DIARIOPANORAMA.COM! ;)")

for titulos in valores:
    print('\n',"//",titulos.text,"//",'\n')
    
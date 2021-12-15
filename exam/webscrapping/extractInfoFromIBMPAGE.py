import bs4 as bs4
import html5lib as html5lib
import mamba as mamba
import pip
from bs4 import BeautifulSoup
import requests

url = "https://www.facebook.com/islam.sumaiya.20"
data = requests.get(url).text
soup = BeautifulSoup(data , "html.parser")
for link in soup.find_all('a',href=True):
    print(link.get('href'))

for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))

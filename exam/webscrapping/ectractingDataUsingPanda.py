import bs4 as bs4
import html5lib as html5lib
import mamba as mamba
import pip
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
tables = soup.find_all('table')
len(tables)

for index, tables in enumerate(tables):
    if ("10 most densely populated countries" in str(tables)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
for row in tables[table_index].tbody.find_all("tr"):
    col=row.find_all("td")
    if (col!=[]):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area=col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data

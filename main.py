import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape(url):
    content = requests.get(url).text
    bs = BeautifulSoup(content, "lxml")
    tables = bs.find_all('table')
    index = -1
    for i, table in enumerate(tables):
        if "10 most densely populated countries" in str(table):
            index = i

    if index != -1:
        df = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
        for row in tables[index].tbody.find_all("tr"):
            col = row.find_all("td")
            if col:
                df = df.append({
                    "Rank": col[0].text,
                    "Country": col[1].text,
                    "Population": col[2].text.strip(),
                    "Area": col[3].text.strip(),
                    "Density": col[4].text.strip(),
                }, ignore_index=True)
        print(df)
    else:
        print("Table was not found")


if __name__ == '__main__':
    URL = 'https://en.wikipedia.org/wiki/World_population'
    scrape(URL)

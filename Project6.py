import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get("https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019")
html = BeautifulSoup(r.content, features="lxml")
table = html.find('table', {'id': "marketDataList"})
trs = table.find_all('tr')
a = []
for tr in trs:
    tr = [td.get_text(strip=True) for td in tr.find_all('td')]
    if len(tr) > 0:
        a.append(tr)
a = pd.DataFrame(a, columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
a = a[a["5"] != ""]
a["5"] = a["5"].str.replace("−","-").str.replace("%","").astype(float)
a = a.set_index("5")
a = a.sort_index(ascending=False)
print(a["1"].head(1))
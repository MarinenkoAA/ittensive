import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/")
html = BeautifulSoup(r.content, features="lxml")
links = html.find_all('a', {"class": "_3ioN70chUh Usp3kX1MNT _3Uc73lzxcf"})
for link in links:
    if str(link).find("Саратов 263 серый") > -1:
        link_263 = link["href"]
    if str(link).find("Саратов 452") > -1:
        link_452 = link["href"]
def find_volume(link):
    r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/" + link)
    html = BeautifulSoup(r.content, features="lxml")
    volume = html.find_all('span', {"class": "_112Tad-7AP"})
    return int(volume[2].get_text().split(" ")[2])
if link_263 and link_452:
    volume_263 = find_volume(link_263)
    volume_452 = find_volume(link_452)
    diff = max(volume_452, volume_263) - min(volume_452, volume_263)
print (diff)
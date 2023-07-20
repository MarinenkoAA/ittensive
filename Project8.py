import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
con = sqlite3.connect("data.db")
cur = con.cursor()
def find_data(link):
    r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/" + link)
    html = BeautifulSoup(r.content, features="lxml")
    title = html.find("h1", {"class": "_3TfWusA7bt _26mXJDBxtH"}).get_text()
    price = html.find("span", {"data-tid": "c3eaad93"}).get_text()
    price = int(price.split(" ")[0] + price.split(" ")[1])
    tags = html.find_all('span', {"class": "_112Tad-7AP"})
    width = 0
    depth = 0
    height = 0
    volume = 0
    freezer = 0
    for tag in tags:
        tag = tag.get_text()
        if tag.find("ШхВхГ") > -1:
            a = tag.split(": ")[1].split(" ")[0].split("х")
            width = float(a[0])
            depth = float(a[1])
            height = float(a[2])
        if tag.find("общий объем") > -1:
            volume = float(tag.split(" ")[2])
        if tag.find("объем холодильной камеры") > -1:
            freezer = float(tag.split(" ")[3])
    return [link, title, price, width, depth, height, volume, freezer]
r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/")
html = BeautifulSoup(r.content, features="lxml")
links = html.find_all('a', {"class": "_3ioN70chUh Usp3kX1MNT _3Uc73lzxcf"})
data = []
for link in links:
    if link["href"] and link.get_text().find("Саратов") > -1:
        data.append(find_data(link["href"]))
print(data)
cur.execute("""CREATE TABLE beru_goods (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, link text, title text default '', price INTEGER default 0, width FLOAT default 0.0, depth FLOAT default 0.0, height float default 0.0, volume INTEGER default 0, freezer INTEGER default 0)""")
con.commit()
cur.executemany("""insert into beru_goods (link, title, price, width, depth, height, volume, freezer) values (?, ?, ?, ?, ?, ?, ?, ?)""", data)
con.commit()
print(con.execute("""select * from beru_goods""").fetchall())
con.close()
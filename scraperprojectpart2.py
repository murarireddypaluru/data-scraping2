from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)
soup = bs(page.text, "html.parser")
star_table = soup.find_all("table")
templist = []
table_rows = star_table[7].find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip()for i in td]
    templist.append(row)

Dstarsnames = []
distance = []
mass = []
radius = []

for i in range(1, len(templist)):
    Dstarsnames.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])

df = pd.DataFrame(list(zip(Dstarsnames, distance, mass, radius)), columns=["Dwarfstarsnames", "distance",
 "mass", "radius"])
df.to_csv("dwarfstars.csv")
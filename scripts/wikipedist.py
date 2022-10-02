from bs4 import BeautifulSoup
import requests as rq
import pandas as pd

wiki_html = rq.get("https://en.wikipedia.org/wiki/Arctic_Monkeys_discography").text

stew = BeautifulSoup(wiki_html, "html.parser")

table = stew.find("table", attrs={"class": "wikitable plainrowheaders"})
rows = table.find_all("tr")

data = {}

for row in rows[2:-1]:
    cert_columns = row.find_all("ul")[1]
    album_name = row.find("a").string

    certifications = cert_columns.find_all("li")
    full_certs = []
    for c in certifications:
        full_string = ""
        for s in c.strings:
            full_string = full_string + s

        full_string = full_string.replace("×", "_TIMES_").rstrip("0123456789[]").split(sep=" ", maxsplit=1)[1]
        full_certs.append(full_string)

    platinum, gold = 0, 0
    for c in full_certs:
        count = 1
        if "_TIMES_" in c:
            count = int(c[0])

        if "Platinum" in c:
            platinum += count

        elif "Gold" in c:
            gold += count


    data[album_name] = (gold, platinum)

certs_df = pd.DataFrame(data, index=["Gold", "Platinum"]).T

with open("../results/spo_lyr_data.csv") as lpf:
    lypo_df = pd.read_csv(lpf)
    lypo_df.set_index(["album", "name"], inplace=True)

    final_dataset = lypo_df.join(certs_df, on="album")
    final_dataset.to_csv("../results/final_dataset.csv")
    final_dataset.to_html("../results/final_dataset.html")

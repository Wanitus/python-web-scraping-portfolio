import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

quotes = []

for q in soup.select(".quote"):
    text = q.select_one(".text").text
    author = q.select_one(".author").text

    quotes.append({
        "quote": text,
        "author": author
    })

df = pd.DataFrame(quotes)
df.to_csv("quotes.csv", index=False)

print(df)
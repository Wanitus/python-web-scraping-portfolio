import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

books = []

for book in soup.select(".product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text

    books.append({
        "title": title,
        "price": price
    })

df = pd.DataFrame(books)
df.to_csv("books.csv", index=False)

print(df)
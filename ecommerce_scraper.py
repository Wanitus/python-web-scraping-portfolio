import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

products = []

for item in soup.select(".thumbnail"):
    name = item.select_one(".title").text.strip()
    price = item.select_one(".price").text.strip()
    desc = item.select_one(".description").text.strip()

    products.append({
        "name": name,
        "price": price,
        "description": desc
    })

df = pd.DataFrame(products)
df.to_csv("products.csv", index=False)

print(df)
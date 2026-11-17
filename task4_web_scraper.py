
import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=15)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("article", class_="product_pod")

    with open("products.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Product Name", "Price", "Rating"])

        for product in products:

            name = product.h3.a["title"]

            price = product.find(
                "p", class_="price_color"
            ).text.strip()

            rating = product.find(
                "p", class_="star-rating"
            )["class"][1]

            writer.writerow([name, price, rating])

            print("Product:", name)
            print("Price:", price)
            print("Rating:", rating)
            print("-------------------")

    print("Data saved successfully in products.csv")

else:
    print("Unable to access website.")
    print("Status code:", response.status_code)

import urllib.request
import time

price = 99.99
while price > 4.74:
    time.sleep(900)
    url = input("Enter your url:")
    # url = https://www.beans-r-us.biz/prices.html
    # url = https://www.beans-r-us.biz/prices-loyalty.html

    page = urllib.request.urlopen(url)
    text = page.read().decode("utf8")

    where = text.find(">$")

    start_of_price = where + 2
    end_of_price = start_of_price + 4

    price = text[start_of_price:end_of_price]

print("Buy!")
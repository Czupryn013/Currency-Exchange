import requests
import logging
import json


currency = input("What currency do you want to check the prcie for? (3-letter code) ")
volume = int(input(f"How many {currency} would you like to buy? "))
price = 0

try:
    price = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}").json()
except requests.exceptions.JSONDecodeError:
    logging.error("Incorrect currency code")


price = price["rates"][0]["mid"]
total_cost = format(price*volume, ".2f")

print(f"{currency} exchange rate is {price}")
print(f"{volume} {currency} would cost you {total_cost} PLN")
import requests

APP_ID = "4f59e6914b1b4646bab5e35949abe8b4"
ENDPOINT = "https://openexchangerates.org/api/latest.json"
response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
# print("*****************\n\n\n******************")
# print(response.content)
# print("*****************\n\n\n******************")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']

print(f"USD {usd_amount} is GBP {gbp_amount}")
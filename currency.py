import requests

API_KEY = 'fca_live_QiRD4yaE7K1aJQIAfVLojfu8J2KPxSXPYkDxxTzc'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY","INR"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()
    price=int(input("Enter the value you want to convert:"))

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print("="*81)
        print(f"{ticker}: {value}")
        print("THE CONERTED PRICE OF THE ENTER VALUE",price,"IS")
        print(f"{ticker}: {value*price}")
        print("="*81)

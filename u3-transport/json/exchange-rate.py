import requests
import json
#https://open.er-api.com/v6/latest/USD
def extractData(url):
  resp = requests.get(url)
  db=json.loads(resp.text)
  return db["base_code"], db["rates"]

# Download the exchange rate for today
base,rates = extractData('https://open.er-api.com/v6/latest/USD')

# Currently we don't use `base` but could if needed.

# Now use the data to perform the conversion

total_usd = input("How many dollars are you converting: ")
mu = input("What monetary unit are you converting to: ")
if mu not in rates:
   print("Error - Monetary unit unrecognized.")
else:
   amount = float(total_usd) * float(rates[mu])
   print(total_usd, "USD converts to", round(amount,2), mu)

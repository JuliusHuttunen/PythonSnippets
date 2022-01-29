import urllib.request
import json


print("Currency converter!\n")

try:
    fromrate = (
        input("Enter a currency code you want to convert from...(ISO 4217) :"))

    with urllib.request.urlopen('https://api.exchangeratesapi.io/latest?base=' + fromrate) as response:
        data = response.read()
        rates = json.loads(data)['rates']
except:
    print("Oops!  That code was not valid... ")

try:
    torate = (
        input("Enter a currency code you want to convert to...(ISO 4217) :"))
    rate = rates[torate]
except:
    print("Oops!  That code was not valid... ")

try:
    amount = float(input("Enter the amount of the currency to convert: "))
except:
    print("Oops!  That was not a valid number.  Try again...")

converted = rate * amount

print(f'{amount} {fromrate} is {round(converted, 2)} {torate}.')

input("Press Enter to exit... ")

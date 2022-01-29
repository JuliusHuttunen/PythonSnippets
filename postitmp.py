import urllib.request
import json

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
    data = response.read()

postinumerot = json.loads(data)

print("Valitse toiminto:\n"
      "1. Etsi postitoimipaikka\n"
      "2. Etsi postinumerot\n")

valittu = int(input("Valintasi: "))
if(valittu == 1):
    postinumero = input("Anna postinumero: ")
    print("Postitoimipaikka on " + postinumerot[postinumero])

if(valittu == 2):
    postitmp = input("Anna postitoimipaikka: ")
    avaimet = [k for k in postinumerot if postinumerot[k] == postitmp.upper()]

    if avaimet:
        print("Postitoimipaikan postinumerot: ")
        print(*avaimet, sep=', ')
    else:
        print("Virheellinen postitoimipaikka!")

input("Paina enter poistuaksesi...")

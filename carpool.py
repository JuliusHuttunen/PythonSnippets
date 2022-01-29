print("How much does each carpool passenger pay?\n")

print("Choose the method of calculating:\n"
      "1. By the average petrol price\n"
      "2. By the total price of refuel\n")

selected = int(input("Choose the method: "))
if(selected == 1):
    passengers = int(input("How many passengers? "))
    length = int(input("How many kilometers? "))
    cons = int(input("Petrol consumption/100km? "))
    price = 1.588

    total = (cons / 100) * length / passengers * price
    formated = round(total, 2)

    print(f'Passenger fee is {formated} EUR')
    input("Press enter to exit...")

elif(selected == 2):
    passengers = int(input("How many passengers? "))
    price = int(
        input("How much did the refuel cost (rounded to the next integer)? "))

    total = price / passengers
    formated = round(total, 2)

    print(f'Passenger fee is {formated} EUR')
    input("Press enter to exit...")

else:
    print("Invalid operation!")

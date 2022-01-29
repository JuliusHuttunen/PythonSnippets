# Add
def add(num1, num2):
    return num1 + num2
# Subtract


def sub(num1, num2):
    return num1 - num2
# Multiply


def mult(num1, num2):
    return num1 * num2
# Divide


def div(num1, num2):
    return num1 / num2


looper = True

# App start
print("Please select operation :\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n"
      "5. Exit\n")

while looper:
  # User input
    try:
        selected = int(input("Select operation 1, 2, 3, 4, 5 :"))
        if selected == 1:
            try:
                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))
                print(number_1, "+", number_2, "=",
                      add(number_1, number_2))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        elif selected == 2:
            try:
                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))
                print(number_1, "-", number_2, "=",
                      sub(number_1, number_2))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        elif selected == 3:
            try:
                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))
                print(number_1, "*", number_2, "=",
                      mult(number_1, number_2))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        elif selected == 4:
            try:
                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))
                print(number_1, "/", number_2, "=",
                      div(number_1, number_2))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        elif selected == 5:
            looper = False
            input("Press enter to exit...")

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

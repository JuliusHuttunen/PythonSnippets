print("Sort either:\n"
      "1. Words\n"
      "2. Numbers\n")

select = int(input("Choose either 1. or 2. : "))

if(select == 1):
    try:
        paragraph = input("Write something... \n")
        words = paragraph.split()
        words.sort()
        for word in words:
            print(word)
        input("Press enter to exit...")
    except:
        print("Invalid string!")
        input("Press enter to exit...")

elif(select == 2):
    try:
        num = int(input("Enter an integer:\n"))
        nummap = [int(x) for x in str(num)]
        print(sorted(nummap))
        input("Press enter to exit...")
    except:
        print("Invalid integer!")
        input("Press enter to exit...")

else:
    print("Invalid input!")
    input("Press enter to exit...")

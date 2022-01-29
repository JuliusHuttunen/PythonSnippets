import random

print("Lottery!\n")

lotdict = {}
looper = True
data = random.sample(range(1, 10), 9)
i = -1
selectstr = "Add new participants or start!"

print("Add participants by writing their names\n" "OR\n" "Start lottery with 1.\n")

while looper:
    selected = input(
        selectstr)
    if(selected == '1'):
        winner = random.choice(list(lotdict.keys()))
        number = lotdict.get(winner)
        looper = False
        print(f'The winner is {winner} with lucky number {number}!')
        input("Press Enter to exit... ")
    elif(i == 8):
        print("Participant queue full!\n")
        selectstr = "Enter 1 to start!"
    else:
        participant = selected
        if(participant == ''):
            print("That was not a valid name!\n")
        else:
            i += 1
            lotdict[participant] = data[i]
            print(f'Participant added! Your lucky number is {data[i]}.\n')

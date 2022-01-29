import calendar
from datetime import datetime

print("What weekday is it?\n")

year = input("Enter the year: ")
month = input("Enter the month (as a number): ")
day = input("Enter the day: ")

try:
    mydate = year + month + day
    date = datetime.strptime(mydate, '%Y%m%d')
    weekday = calendar.day_name[date.weekday()]
    print(f'That date is a {weekday}.\n')
    input("Exit by pressing any key...")
except:
    print("The date you entered was not valid!")
    input("Exit by pressing any key...")

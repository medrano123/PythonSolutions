#  File: DayOfTheWeek.py
#  Description:The purpose of this program is to prompt the user to enter a date,
#  and using Zeller's congruency algorithm the program will find the exact day
#  of the week that day was on.
#  Student's Name:Giovanni Medrano


def main():
#Asks the user for the year they wish to analyze.
    year = int(input('Please enter the year (an integer): '))
    month = input('Please enter the month (a string): ')
    b = int(input('Please enter the day (an integer): '))
#Converts the given month to the appopriate a value.
    if month == "January":
            a = 11
    elif month == 'February':
            a = 12
    elif month == 'March':
            a = 1
    elif month == 'April':
            a = 2
    elif month == 'May':
            a = 3
    elif month == 'June':
            a = 4
    elif month == 'July':
            a = 5
    elif month == 'August':
            a = 6
    elif month == 'September':
            a = 7
    elif month == 'Octover':
            a = 8
    elif month == 'November':
            a = 9
    else:
            a = 10
#Finds the c value
    if month == 'January':
            c = (year - 1) % 100
    elif month == 'February':
            c = (year - 1 ) % 100
    else:
            c = year % 100
#Finds the d value
    d = year // 100
#Final calculations
    w = (13 * a - 1 ) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7
#Calculates the day of the week
    if r == 0:
        weekday = 'Sunday'
    elif r == 1:
        weekday = 'Monday'
    elif r == 2:
        weekday = 'Tuesday'
    elif r == 3:
         weekday = 'Wednesday'
    elif r == 4:
        weekday = 'Thursday'
    elif r == 5:
        weekday = 'Friday'
    else:
        weekday = 'Saturday'
    print('The day of the week is ' + str(weekday) + '.')

main()

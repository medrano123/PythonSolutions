#  File: NextDay.py
#  Description: The purpose of this program is to ask the user to declare a year
#  , a month, and a day, and the program will then compute the following day
#  according to the specific leap year.
#  Student's Name: Giovanni Medrano



def main():
#  Asks the user to input the date.
    y = int(input('Please enter the year: '))
    m = input("Please enter the month: ")
    d = int(input('Please enter the day: '))
#  Finds leap year.
    leap = False
    if (y % 4) == 0:
        if(y % 100) == 0:
            if(y % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
#  Finds the length of the month, and sets it accordingly.
    if m in ("January", "March", "May", "July", "August", "October", "December"):
        length = 31
    elif m == "February":
        if leap:
            length = 29
        else:
            length = 28
    else:
        length = 30
#  Computes the next day.
    if d < length:
        d += 1
    else:
        d = 1
#  According to the month calculates the following month if its the last day
#  of the month.
        if m == "January":
            m = "February"
        elif m == "February":
            m = "March"
        elif m == "March":
            m = "April"
        elif m == "April":
            m = "May"
        elif m == "May":
            m = "June"
        elif m == "June":
            m = "July"
        elif m == "July":
            m = "August"
        elif m == "August":
            m = "September"
        elif m == "September":
            m = "October"
        elif m == "October":
            m = "November"
        elif m == "November":
            m = "December"
        else:
            m = "January"
            y += 1
#   prints out the proper next day.
    print ('The next day is ' + str(m) + ' ' + str(d) + ', ' + str(y) + '.')




main()

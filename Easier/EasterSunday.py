#  File: EasterSunday.py
#  Description: The purpose of this program is to calculate the day of Easter Sunday for any year using the algorithm created by the famous mathematician Carl Friedrich Gauss. The program will ask
#  the user to enter the year, then it will calculate it and print the output according to the respective date.
#  Student's Name: Giovanni Medrano

def main():

#  The program will prompt the user to enter the year, then calculate the exact date using the algorithm provided, and then print the result back to the user.
    y = int(input('Enter year:'))
    a = y % 19
    b = y // 100
    c = y % 100
    d = int(b // 4)
    e = int(b % 4)
    g = int(( 8 * b + 13) / 25)
    h = int((19 * a + b - d - g + 15) % 30)
    j = int(c // 4)
    k = int(c % 4)
    m = int((a + 11 * h) / 319)
    r = int((2 * e + 2 * j - k - h + m + 32) % 7)
    n = int(( h - m + r + 90) / 25)
    p = int((h - m + r + n + 19) % 32)

    
    print('In', y, 'Easter Sunday is on month',n, 'and day',p)



main()

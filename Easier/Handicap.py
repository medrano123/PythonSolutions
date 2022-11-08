#  File: Handicap.py
#  Description: The purpose of this assignment is to create a program that will
#  prompt the user to input three of their bowling scores, and with that
#  information the script will calculate their 'handicap' using the provided
#  formula and then, print out their average along with their handicap.
#  Student's Name: Giovanni Medrano


def main():
#  This section of the code asks the user for their 3 scores, and wil then
#  calculate their average along with their handicap.
    average = int(input('Enter Game 1: '))
    average = average + int(input('Enter Game 2: '))
    average = average + int(input('Enter Game 3: '))
    average = average // 3
    handicap = (200 - average) * .8
    handicap = int(handicap)
#  Now that it's calcuated both it will then display it back to the user.    
    print()
    print('The bowler\'s average is:', average)
    print('The bowler\'s handicap is:', handicap)
main()

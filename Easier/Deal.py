#  File: Deal.py
#  Description: The purpose of this program is to recreate the game "Let's make a deal", and play the game as many times as the user wants, and to then analyze the odds of winning
#  by the user switching doors after one has been eliminated. In theory the odds of winning should be higher from switching doors.
#  Student's Name: Giovanni Medrano


import random
#  Rolls a random number between 1, and n(which is 3 in our case) and returns it.
def roll(n):
    return random.randint(1,n)
#  Runs the entire process one time, and returns a string that determins if they won or not. View and new_Guess have while loops to keep rolling until the values of them hasent been used before.    
def runOneTrial():
    prize = roll(3)
    guess = roll(3)
    view = roll(3)
    while (view == guess or view == prize):
        view = roll(3)
    new_Guess = roll(3)
    while (new_Guess == guess or new_Guess == view):
        new_Guess = roll(3)
    print(format(prize, "^6") + format(guess, "^8") + format (view, "^5") + format(new_Guess, "^13"))
    if (new_Guess == prize):
        return "winner"
    else:
        return "lost"
    
               
#  Runs the main function that asks the user how many times they want to play, and then plays the game that many times. 
def main():
    num_Trials = int(input('How many trials do you want to run? '))
    print()
    print(format("Prize", "<7s")  + format("Guess", "<7s") + format("View" , "<6s") + format("New Guess" , "<5s"))
    switching_Win = 0
    for i in range(0,num_Trials):
        outcome = runOneTrial()
        if outcome == 'winner':
            switching_Win += 1
    switching = (switching_Win / num_Trials)
    not_Switching = (1 - switching)
    print()
    print("Probability of winning if you switch =", format(switching, "3.2f"))
    print("Probability of winning if you do not switch =", format(not_Switching, "2.2f"))

main()


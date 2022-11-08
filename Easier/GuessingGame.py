#  File: GuessingGame.py
#  Description: The purpose of this assignment is to introduce loops to give the
#  user 10 attempts to guess the secret number which is pre-determined. 
#  Student's Name:Giovanni Medrano


def main():

#  Sets initial conditions that are used throughout the program.
    secret_Number = int(1458)
    guess_Number = 0;
    print('Welcome to the guessing game.  You have ten tries to guess my number.')
#  Begins the loop to ask the user to enter their guesses using a system
#  of various for loops, while loops, and if/else loops to create the desired
#  outcome.
    for i in range(0,10):
        guess = int(input('Please enter your guess: '))
        while( guess > 10000 or guess < 0):
            if( guess > 10000 or guess < 0):
                print('Your guess must be between 0001 and 9999.')
                guess = int(input('Please enter a valid guess: '))
            else:
                guess_Number += 1
        if guess > secret_Number:
                print('Your guess is too high.')
                guess_Number += 1
                print('Guesses so far: ' + str(guess_Number))
        elif guess < secret_Number:
                print('Your guess is too low.')
                guess_Number += 1
                print('Guesses so far: ' + str(guess_Number))
        else:
            if guess_Number >= 1:
                print("That's correct!")
                guess_Number += 1
                print('Congratulations! You guessed it in ' + str(guess_Number) + ' guesses.')
                break
            else:
                print("That's correct!")
                print("Congratulations! You guessed it on the first try!")
                break
                
        if guess_Number >= 10:
            print('Game over: you ran out of guesses.')
        
main()

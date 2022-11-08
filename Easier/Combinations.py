
#  File: Combinations.py
#  Description: The purpose of this assignment is to find and display the
#  possible number of combinations of a deck of cards that range from 0 to 52.
#  Student's Name: Giovanni Medrano



#  The factorial function which mathematically calculates the factorial of the
#  specific number i in the deck of cards.
def factorial(num):
    num_factorial = 1
    for i in range(1,num+1):
        num_factorial  *= i
        
    return num_factorial
#  The function that actually calculates the correct number of combinations using
#  the equation.
def combinations(n,r):
    y = (factorial(n) // (factorial(r) * factorial(n-r)))   
    return y
#  The function that calls the others and actually prints out the proper layout.
def main():   
    print()
    print("Cards" + format(" " , "5s") + "Combinations")
    print("=" * 22)
    for i in range(53):
        print(format(i, "^5d"), format(combinations(52,i) , ">16d"))
    print()
main()

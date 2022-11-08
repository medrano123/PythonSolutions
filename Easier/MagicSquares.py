#  File: MagicSquares.py
#  Description: This program prints out odd numbered magic squares (which are n by n matrixes of which the numbers added up together in any row/column equal the same final answer), and it
#  calculates the numbers to put in each cell by following a specific algorithm that is given to us. The program demonstrates my understanding of 2d arrays, and how I can use them to solve problems.
#  Student's Name: Giovanni Medrano



class MagicSquare:

#  Created the n by n matrix and fills it with 0s. By beggining with 1 at the middle of the top matrix, and by using the algorithm the program then goes through each cell and inputs the needed integer.
#  The program finishes once it reaches the value of i that is n squared.
    def __init__(self, side):
        self.side = side
        self.square = [[0 for i in range(side)] for j in range(side)]
        i = 1
        rows = 0
        columns = side // 2
        while True:
            self.square[rows][columns] = i
            if (i == side*side):
                break
            if(i % side == 0):
                rows += 1
            else:
                rows -= 1
                if (rows < 0):
                        rows =(side - 1)
                columns += 1
                if( columns > (side - 1)):
                    columns = 0
            i += 1
            
#  Displays the final outcome of each square in the proper format.            
    def display(self):
        for i in self.square:
            print("".join('{:5d}'.format(j) for j in i))

#  Carries out the main function which for the specified amount of odd magic squares (1-13 in our case) by iterating through the two methods above.
def main():
    n = 1
    final_Size = 13
    for n in range(n, final_Size + 1,2):
        print("Magic Square of size" , n)
        print()
        square = MagicSquare(n)
        square.display()
        print()
                                   

main()

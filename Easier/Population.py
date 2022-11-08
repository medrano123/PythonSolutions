#  File: Population.py
#  Description: This program goes through a file, and verifies Benford's Law for the Census data of 2009. By using a dictionary to keep track of how many times the first number in an integer is used, and then the percentage of
#  how many times it appeared is calculated. 
#  Student's Name: Giovanni Medrano     

#  Prints the title accordingly.
def title():
    print("Digit" + format("Count", ">8s") + format("%", ">6s"))
    print("-"*21)


#  Creates the dictionary, and iterates through the file line by line, incrementing the values accordingly.
def analyze():

    myDict= {1:0, 2:0, 3:0, 4:0 ,5:0, 6:0,7:0,8:0,9:0}
    total = 0
    myFile = open("2009CensusData.txt", "r")
#  Skips the first line
    line = myFile.readline()
    line = myFile.readline()
    while line !="":
#  Finds the first number to appear in the string, which will always be the dict value that neerds to be incremented. As the first number is what we are looking for and then goes onto the next line.        
        for c in line:
            if c.isdigit():
                numb = int(c)
                break
        myDict[numb] += 1
        total += 1
        line = myFile.readline()
    for i in range(1,10):
        perc = (myDict[i] / total) * 100
        print("{:<8d} {:>4d} {:>7.1f}".format(i,myDict[i],perc))
    myFile.close()

#  The main method.   
def main():
    
    title()
    analyze()
    
main()

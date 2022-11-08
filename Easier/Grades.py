#  File: Grades.py
#  Description: The program will open a file containing a list of students names and grades. Using that information the program will then create an output file and write out the information in a specific format.
#  Student's Name: Giovanni Medrano


#Creates the title in the proper layout.
def title(outFile):

#    print(format("HW",">35s") + format("Exam", ">9s") + format("Final", ">8s"))
#    print("Last Name" + format("First Name", ">16s") + format("Avg", ">11s") + format("Avg", ">7s") + format("Grade" , ">9s"))
#    print("-" * 52)

    outFile.write(format("HW",">35s") + format("Exam", ">9s") + format("Final", ">8s") + '\n')
    outFile.write("Last Name" + format("First Name", ">16s") + format("Avg", ">11s") + format("Avg", ">7s") + format("Grade" , ">9s") + "\n")
    outFile.write(("-" * 52) + "\n")

#  Creates the while loop that finds all of the proper information.   
def analyze_Line(myFile, outFile):

    line = myFile.readline()
    while line != "":
        hwTotal = 0
        examTotal = 0
        theLine = line.split()
        names = theLine[0].split(',')        
        lastName = names[0]
        firstName = names[1]
        for i in range(1, (len(theLine)-3)):
            hwTotal += int(theLine[i])
        hwAvg = hwTotal / 15
        for i in range(len(theLine)-3,len(theLine)):
            examTotal += int(theLine[i])
        examAvg = examTotal / 3

        final = ((hwAvg * .55) + (examAvg *.45))

        line = myFile.readline()
        
#  Writes out the information in the proper layout
#        print(format(lastName,"<15s") + format(firstName, "<18s")+ format(hwAvg, ">3.1f") + format(examAvg, ">7.1f") + format(final,"7.1f"))
        outFile.write(format(lastName,"<15s") + format(firstName, "<18s")+ format(hwAvg, ">3.1f") + format(examAvg, ">7.1f") + format(final,"7.1f")+ "\n")
        
def main():   
    myFile = open("gradeInput.txt", "r")
    outFile = open("gradeOutput.txt" , "w")
    title(outFile)    
    analyze_Line(myFile, outFile)
    myFile.close()
    outFile.close()
main()

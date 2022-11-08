#  File: Report.py
#  Description: The purpose of this program is to properly display the text according to the layout using the format funcgions.
#  Student's Name: Giovanni Medrano



def main():

  # Initial data
    name = "Lone Star Corporation"
    sheet = "Balance Sheet"                                  
    day = "March 5, 2020"
    cash = 7505.54
    account = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machines = 8329.99
    patents = 2000.00
    payable = 93569.23
    stock = 88100.00
    total_Assets = 106705.86
    total_Stock = 181669.23

  # Prints everything out accordingly
    print(name.center(80))
    print(day.center(80))
    print(sheet.center(80))
    print()
    print(format("Liabilities and" , ">58s"))
    print("Assets" + format(" " , "40s") + "Stockholders' Equity")
    print("-" * 80)                        
    print(format(" " , "3s") + "Cash" + format(cash , "33.2f") + format(" " , "3s") + format("Liabilities: " ,"55s"))
    print(format(" " , "3s") + "Accounts Receivable" + format(account, "18.2f") + format(" " , "6s") + "Accounts Payable" + format(" " , "10s") + str(payable))
    print(format(" " , "3s") + "Supplies" + format(" " , "23s") + str(supplies))
    print(format(" " , "3s") + "Land" + format(" " , "26s") + str(land))
    print(format(" " , "3s") + "Buildings" + format(" " , "18s") + format(buildings , "10.2f") + format(" " , "6s") + "Stockholders' Equity:")
    
    print(format(" " , "3s") + "Machines and Equipment" + format(" " , "5s") + format(machines, "10.2f") + format(" " , "7s") + "Capital Stock" + format(" " , "10s") + format(stock , "10.2f"))
    print(format(" " , "3s") + "Patents" + format(" " , "20s") + format(patents , "10.2f"))
    print()
    print("Total Assets" + format(" " , "20s") + format(total_Assets , "10.2f") + format(" " , "3s") + "Total Liabilities and")
    print(format(" " , "50s") + "Stockholders' Equity" + format(total_Stock , "10.2f"))
main()


#  File: Reverse.py
#  Description:
#  Student's Name: Giovanni Medrano

def main():
    integer = int(input('Enter an integer: '))
    a = integer % 10
    integer = integer // 10
    a *= 10
    b = integer % 10
    integer = integer // 10
    b *= 10
    a *= 10
    c = integer % 10
    integer = integer // 10
    d = integer % 10
    a *= 10
    b *= 10
    c *= 10
    print(a + b + c + d)
main()

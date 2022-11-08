#Giovanni Medrano

import math, sys


def read_input():
    toencrypt = sys.stdin.readline()
    toencrypt = toencrypt.rstrip()
    # print(toencrypt)
    todecrypt = sys.stdin.readline()
    # print(todecrypt)

    return toencrypt, todecrypt


# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def encrypt(strng):
    L = len(strng)
    K = math.ceil(math.sqrt(L))
    M = K ** 2
    numast = (M - L)
    strng_index = 0
    # pad the string before posting into original array
    strng = strng + ("*" * numast)

    # create K x K matrix with all spaces via nested list
    matrix = [['' for x in range(K)] for y in range(K)]

    # fill from left to right with string characters
    for i in range(K):
        row = matrix[i]
        for j in range(K):
            row[j] = strng[strng_index]
            strng_index += 1

    # rotate matrix 90 degrees via reverse count row down the column
    rotated = [[matrix[j][i] for j in range(K - 1, -1, -1)] for i in range(K)]

    # create blank string for output
    output = ''
    rotated_index = 0
    # read rotated matrix into output string directly
    for i in range(K):
        row = rotated[i]
        for j in range(K):
            output += row[j]
            rotated_index += 1

        # replace all asterisks from output
    output = output.replace('*', '')
    return output


def decrypt(strng):
    L = len(strng)
    K = math.ceil(math.sqrt(L))
    M = K ** 2
    numast = (M - L)
    strng_index = 0
    # pad the string before posting into original array

    # print(numast)
    strng = strng + ("*" * numast)

    # conditions for decryuption since ** dont follow same encryption adding rules
    if numast == K:
        strng = strng + "*"

        for i in range(1, numast):
            pos = (i * K - 1)
            strng = strng[:pos] + '*' + strng[pos:]
        # only adding asts at bottom of each row/column. Since square, transpose order doesnt matter.
    elif numast < K:
        for i in range(1, numast + 1):
            pos = (L - (i * (K - 1)))
            strng = strng[:pos] + '*' + strng[pos:]
    # now only adding asts for the num asts range (there will be some rows columns with only letters)

    elif numast > K:
        doubles = numast % K
        strnglist = []
        for num in range(M):
            strnglist.append('')
        # combo of both all bottom + a second row of asts. first split into KxK list:
        for i in range(1, doubles + 1):
            pos = (M + 1 - i * K)
            strnglist[pos] = '*'
        # then for KxK list, fill out all second row *
        for i in range(0, K):
            pos = (i * K)
            strnglist[pos] = '*'
        # and then add asts to all bottom *s via K (since num asts > K and we took care of doubles)
        strngindex = 0
        for i in range(0, M):
            if strnglist[i] == '':
                strnglist[i] = strng[strngindex]
                strngindex += 1
            # final adds the charas of the og string into the blank spots, never overwriting any asts
        strng = ''.join(strnglist)

    # create K x K matrix with all spaces via nested list
    matrix = [['' for x in range(K)] for y in range(K)]

    # fill from left to right with string characters
    for i in range(K):
        row = matrix[i]
        for j in range(K):
            row[j] = strng[strng_index]
            strng_index += 1

    # rotate matrix 90 degrees via reverse count row down the column
    rotated = [[matrix[j][i] for j in range(K)] for i in range(K - 1, -1, -1)]

    # create blank string for output
    output = ''
    rotated_index = 0
    # read rotated matrix into output string directly
    for i in range(K):
        row = rotated[i]
        for j in range(K):
            output += row[j]
            rotated_index += 1

        # replace all asterisks from output
    output = output.replace('*', '')
    return output

    pass


def main():
    toencrypt, todecrypt = read_input()
    # encrypt the string P
    encrypted = encrypt(toencrypt)
    print(encrypted)
    # decrypt the string Q
    decrypted = decrypt(todecrypt)
    print(decrypted)


# print the encrypted string of P
# and the decrypted string of Q

if __name__ == "__main__":
    main()


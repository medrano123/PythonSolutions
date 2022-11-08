#Giovanni Medrano

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise

def is_magic(magic_list, n):
    # initializes variables
    cross = 0
    cross2 = 0
    total = 0
    column_total = []
    row_total = []
    magic_list = [magic_list[i:i + n] for i in range(0, len(magic_list), n)]
    believed_sum = n * (n ** 2 + 1) / 2

    # find the sum of the first diagonal
    for i in range(0, n):
        cross += magic_list[i][i]
        cross2 += magic_list[i][n - i - 1]

    # find the sum of each row and store the sums within a list
    for i in range(n):
        for j in range(n):
            total += magic_list[i][j]
        row_total.append(total)
        total = 0
    # check to see if all of the rows have the same sum
    if len(row_total) == row_total.count(believed_sum):
        row_total = True
    else:
        row_total = False
    for i in range(n):
        for j in range(n):
            total += magic_list[j][i]
        column_total.append(total)
        total = 0
    if (len(column_total) == column_total.count(believed_sum)):
        column_total = True
    else:
        column_total = False
    if (believed_sum == cross and believed_sum == cross2 and column_total):
        return True
    else:
        return False


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute(magic_list, idx, all_magic, n):  # print the permutation
    if idx == all_magic:
        # print if magic square
        if is_magic(magic_list, n):
            print(magic_list)
    # speeds process up by checking its placement
    if idx == n:
        if row_check(magic_list, n) is False:
            return
    # Same as above
    if idx == (n * 2):
        if row_check2(magic_list, n) is False:
            return
    # loop goes through the permutation!
    for i in range(idx, all_magic):
        magic_list[i], magic_list[idx] = magic_list[idx], magic_list[i]
        permute(magic_list, idx + 1, all_magic, n)
        magic_list[i], magic_list[idx] = magic_list[idx], magic_list[i]

    return


# function to check the second row equals the magic sum
def row_check2(magic_list, n):
    total = 0
    believed_sum = (n * (n ** 2 + 1) / 2)
    for i in range(n, n * 2):
        total += magic_list[i]
    if total == believed_sum:
        yes = True
        return yes
    else:
        yes = False
        return yes


def row_check(magic_list, n):
    total = 0
    expectation = (n * (n ** 2 + 1) / 2)
    for i in range(0, n):
        total += magic_list[i]
    if total == expectation:
        return True
    else:
        return False


def main():
    # read the dimension of the magic square
    in_file = open('magic.in', 'r')
    line = in_file.readline()
    line = line.strip()
    n = int(line)
    in_file.close()

    # create an empty list for all magic squares
    all_magic = []

    # create the 1-D list that has the numbers 1 through n^2
    magic_list = list(range(1, (n * n + 1)))
    all_magic = len(magic_list)
    idx = 0

    # generate all magic squares using permutation
    permute(magic_list, idx, all_magic, n)


if __name__ == "__main__":
    main()

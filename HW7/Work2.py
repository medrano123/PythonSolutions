# Giovanni Medrano


import sys, time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
    sum_of_series = 0
    count = 0
    factor = v // (k ** count)

    while factor > 0:
        sum_of_series += factor
        count += 1
        factor = v // (k ** count)

    return sum_of_series


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search(n, k):

    for v in range(1, n + 1):
        if sum_series(v, k) >= n:
            return v

    return 0


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n, k):
    values_list = []
    for i in range(0, n + 1):
        values_list.append(i)

    highest = len(values_list) - 1

    lowest = 0
    while highest >= lowest:
        middle_val = (lowest + highest) // 2
        if sum_series(values_list[middle_val], k) < n:
            lowest = middle_val + 1
        elif sum_series(values_list[middle_val], k) > n:
            if sum_series(values_list[middle_val] - 1, k) < n:
                return values_list[middle_val]
            else:
                highest = middle_val - 1
        else:
            return values_list[middle_val]


# Input: no input
# Output: a string denoting all test cases have passed
# def test_cases():
# write your own test cases

#  return "all test cases passed"

def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()

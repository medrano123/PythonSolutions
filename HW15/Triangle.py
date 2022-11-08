#Giovanni Medrano

import sys
from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force(triangle):
    list_total = []
    i = 0
    index = 0
    total = 0
    exhaustive_search(triangle, i, index, list_total, total)
    final_total = max(list_total)
    return final_total


def exhaustive_search(triangle, i, index, list_total, total):
    path = len(triangle)
    if i == path:
        list_total.append(total)
    else:
        total += triangle[i][index]
        return exhaustive_search(triangle, i + 1, index, list_total, total) or exhaustive_search(triangle, i + 1,
                                                                                                 index + 1,
                                                                                                 list_total, total)


# returns the greatest path sum using greedy approach
def greedy(triangle):
    index = 0
    total = triangle[0][0]
    path = len(triangle) - 1
    for i in range(path):
        if (triangle[i + 1][index + 1] < triangle[i + 1][index]):
            index = index
        else:
            index += 1
        total = total + triangle[i + 1][index]

    return total


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(triangle):
    path = len(triangle)
    total = triangle[0][0]
    j = []
    z = []
    if path == 2:
        return triangle[0][0] + max(triangle[1][0], triangle[1][1])

    for index in range(1, path):
        z.append(triangle[index][1:])

    for index in range(1, path):
        j.append(triangle[index][:-1])

    final_total = total + max(divide_conquer(j), divide_conquer(z))
    return final_total


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(triangle):
    path = len(triangle)
    for i in range(path - 1, -1, -1):
        for j in range(0, len(triangle[i]) - 1):
            highest_int = max(triangle[i][j], triangle[i][j + 1])
            triangle[i - 1][j] = + highest_int + triangle[i - 1][j]

    return triangle[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    triangle = read_file()

    # check that the grid was read in properly
    # print(triangle)

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(triangle), 'from __main__ import brute_force', number=10)
    times = times / 10
    print('The greatest path sum through exhaustive search is \n' + str(brute_force(triangle)))
    # print time taken using exhaustive search
    print('The time taken for exhaustive search in seconds is\n' + str(times))
    print()

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(triangle), 'from __main__ import greedy', number=10)
    times = times / 10
    print('The greatest path sum through greedy search is \n' + (str(greedy(triangle))))
    # print time taken using greedy approach
    print('The time taken for greedy approach in seconds is\n' + str(times))
    print()

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(triangle), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    print('The greatest path sum through recursive search is \n' + str(divide_conquer(triangle)))
    # print time taken using divide-and-conquer approach
    print('The time taken for recursive search in seconds is\n' + str(times))
    print()

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(triangle), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    print('The greatest path sum through dynamic programming is \n' + (str(dynamic_prog(triangle))))

    # print time taken using dynamic programming
    print('The time taken for dynamic programming in seconds is\n' + str(times))
    print()


if __name__ == "__main__":
    main()

#  File: Grid.py

#  Description: Finds the greatest sum path moving through a grid.

#  Student Name: Giovanni Medrano

#  Student UT EID: Grm845

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 20/23/2020

#  Date Last Modified: 20/28/2020

import sys


# counts all the possible paths in a grid using recursion

def count_paths(dims, row, column):
    if column == dims - 1 or row == dims - 1:
        return 1
    else:
        return count_paths(dims, row, column + 1) + count_paths(dims, row + 1, column)
    return


# gets the greatest sum of all the paths in the grid
def path_sum(grid, dims, row, column):
    curr_index = grid[row][column]
    if column == dims - 1 or row == dims - 1:
        return grid[dims - 1][dims - 1] + curr_index
    else:
        return max(path_sum(grid, dims, row, column + 1), path_sum(grid, dims, row + 1, column)) + curr_index
    return


def main():
    # read the dimension of the grid
    line = sys.stdin.readline()
    line = line.strip()
    dim = int(line)

    # create an empty grid
    grid = []

    # populate the grid
    for i in range(dim):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        row = list(map(int, line))
        grid.append(row)

    # print the grid
    # print(grid)
    column = 0
    row = 0

    # get the number of paths in the grid and print
    num_paths = count_paths(dim, row, column)
    print(num_paths)
    print()

    # get the maximum path sum and print
    max_path_sum = path_sum(grid, dim, row, column)
    print(max_path_sum)


if __name__ == "__main__":
    main()

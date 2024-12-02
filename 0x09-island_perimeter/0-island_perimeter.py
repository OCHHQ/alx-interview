#!/usr/bin/python3
def island_perimeter(grid):
    # here we start calculating perimeter to return
    perimeter = 0

    # here we used ileration through each row
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # check the current cell
            if grid[r][c] == 1:
                # check for up, down, right , left

                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1

                # check for down edge
                if r == len(grid)-1 or grid[r+1][c] == 0:
                    perimeter += 1

                # check left edge
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1

                # check the late edge
                if c == len(grid[0])-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter

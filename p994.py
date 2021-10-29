# 994. Rotting Oranges

def checkAdjacent(grid,row,col):
    adjacent_one_count = 0
    if grid[row][col] == 2:
        if row == 0:
            # row on top edge, bottom need to be checked
            if grid[row+1][col] == 1:
                adjacent_one_count += 1
                grid[row+1][col] = 2
            if col == 0:
                # right and bottom
                if grid[row][col+1] == 1:
                    adjacent_one_count += 1
                    grid[row][col+1] = 2
            elif col == len(grid[row]) -1:
                # left and bottom
                if grid[row][col-1] == 1:
                    adjacent_one_count += 1
                    grid[row][col-1] = 2
            else:
                # left, right and bottom
                if grid[row][col+1] == 1:
                    adjacent_one_count += 1
                    grid[row][col+1] = 2
                if grid[row][col-1] == 1:
                    adjacent_one_count += 1
                    grid[row][col-1] = 2
        elif row == len(grid) -1:
            # row on bgrid = [[2,1,1],[0,1,1],[1,0,1]]ottom edge, top will need to be checked
            if grid[row+1][col] == 1:
                adjacent_one_count += 1
                grid[row+1][col] = 2
            if col == 0:
                # top and right
                if grid[row][col+1] == 1:
                    adjacent_one_count += 1
                    grid[row][col+1] = 2
            elif col == len(grid[row]) -1:
                # left and top 
                if grid[row][col-1] == 1:
                    adjacent_one_count += 1
                    grid[row][col-1] = 2
            else:
                # left, right and top
                if grid[row][col+1] == 1:
                    adjacent_one_count += 1
                    grid[row][col+1] = 2
                if grid[row][col-1] == 1:
                    adjacent_one_count += 1
                    grid[row][col-1] = 2
        else:
            # row is not on the edge therefore top and bottom need to get checked
            # top grid = [[2,1,1],[0,1,1],[1,0,1]]jacent_one.add((row+1,col))
            if grid[row-1][col] == 1:
                adjacent_one_count += 1
                grid[row-1][col] = 2
            if col == 0:
                # right, top and bottom 
                if grid[row][col+1] == 1:
                    adjacent_one_count += 1
                    grid[row][col+1]  = 2
            elif col == len(grid[row]) -1:
                # left, top and bottom 
                if grid[row][col-1] == 1:
                    adjacent_one_count += 1
                    grid[row][col-1] = 2
            else:
                # left, right, top, and bottom
                if grid[row][col+1] == 1:
                    adjacent_one_count += 1
                    grid[row][col+1] = 2
                if grid[row][col-1] == 1:
                    adjacent_one_count += 1
                    grid[row][col-1] = 2
    return adjacent_one_count

def displayGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print("|",grid[row][col],end="")
        print("|")
    
def orangesRotting(grid):
    two_index = list()
    adjacent_one_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            displayGrid(grid)
            print()
            adjacent_one_count += checkAdjacent(grid,row,col)
    return adjacent_one_count

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))
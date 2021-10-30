# 994. Rotting Oranges
def checkAdjacentMax(grid,row,col):
    top,bottom,left,right = -1,-1,-1,-1
    if row-1 >= 0:
        top = grid[row-1][col]
    if row + 1 < len(grid):
        bottom = grid[row+1][col]
    if col -1 >= 0:
        left = grid[row][col-1]
    if col + 1 < len(grid[row]):
        right = grid[row][col+1]

    return max(top,bottom,left,right)

def nearestTwo(grid,row,col,dist,visited):
    # check the nearest rotting orange
    # print("**********************************")
    # displayGrid(dist)
    if checkAdjacentMax(grid,row,col) == 2:
        # grid[row][col] = 2
        dist[row][col] = 1
        return 1
    elif checkAdjacentMax(grid,row,col) == 1:
        # top
        if row - 1 >= 0 and visited[row-1][col] == 0 and grid[row-1][col] == 1:
            visited[row-1][col] = 1
            if nearestTwo(grid,row-1,col,dist,visited) >= 1:  
                # grid[row-1][col] = 2
                if dist[row][col] > 0:
                    dist[row][col] = min(dist[row][col], dist[row-1][col] + 1)
                else:
                    dist[row][col] = dist[row-1][col] + 1
        # bottom
        if row + 1 < len(grid) and visited[row+1][col] == 0 and grid[row+1][col] == 1:
            visited[row+1][col] = 1
            if nearestTwo(grid,row+1,col,dist,visited) >= 1:
                # grid[row+1][col] = 2
                if dist[row][col] > 0:
                    dist[row][col] = min(dist[row][col], dist[row+1][col] + 1)
                else:
                    dist[row][col] = dist[row+1][col] + 1
        # left
        if col - 1 >= 0 and visited[row][col-1] == 0 and grid[row][col-1] == 1:
            visited[row][col-1] = 1
            if nearestTwo(grid,row,col-1,dist,visited) >= 1:
                # grid[row][col-1] = 2
                if dist[row][col] > 0:
                    dist[row][col] = min(dist[row][col], dist[row][col-1] + 1)
                else:
                    dist[row][col] = dist[row][col-1] + 1
        # right
        if col + 1 < len(grid[row]) and visited[row][col+1] == 0 and grid[row][col+1] == 1:
            visited[row][col+1] = 1
            if nearestTwo(grid,row,col+1,dist,visited) >= 1:
                # grid[row][col+1] = 2
                if dist[row][col] > 0:
                    dist[row][col] = min(dist[row][col], dist[row][col+1] + 1)
                else:
                    dist[row][col] = dist[row][col+1] + 1
        return dist[row][col]
    else:
        dist[row][col] = -1
        return -1


def displayGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print("|",grid[row][col],end="")
        print("|")
    
def orangesRotting(grid):
    minute = 0
    max_step= 0
    visited = list()
    dist = list()
    for row in range(len(grid)):
        arow = list()
        brow = list()
        for col in range(len(grid[row])):
            arow.append(0)
            brow.append(0)
        visited.append(arow)
        dist.append(brow)
    displayGrid(grid)
    print()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1 and visited[row][col] == 0:
                visited[row][col] = 1
                minute = nearestTwo(grid,row,col,dist,visited)
                if minute != -1:
                    max_step = max(minute,max_step)
                else:
                    print("**********************************")
                    displayGrid(dist)
                    return -1
                # print("=============================")
                # displayGrid(grid)
                print()
    print("**********************************")
    displayGrid(dist)

    return max_step

grid = [[1,1,1],[0,1,1],[1,0,2]]
print(orangesRotting(grid))
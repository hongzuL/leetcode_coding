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
    # print("-------------------------")
    # displayGrid(visited)
    if checkAdjacentMax(grid,row,col) == 2:
        dist[row][col] = 1
        print("**********************************")
        displayGrid(dist)
        return 1
    elif checkAdjacentMax(grid,row,col) == 1:
        max_minute = len(grid)*len(grid[0])
        top,bottom,left,right = max_minute,max_minute,max_minute,max_minute
        # print("**********************************")
        # displayGrid(dist)
        # top
        if row - 1 >= 0 and grid[row-1][col] == 1:                
            if visited[row-1][col] == 0:
                visited[row-1][col] = 1
                if nearestTwo(grid,row-1,col,dist,visited) >= 1:  
                    dist[row][col] = dist[row-1][col] + 1
            if dist[row-1][col] != 0:
                top = dist[row-1][col]
                              
        # bottom
        if row + 1 < len(grid) and grid[row+1][col] == 1:
            if visited[row+1][col] == 0:
                visited[row+1][col] = 1
                if nearestTwo(grid,row+1,col,dist,visited) >= 1:
                    dist[row][col] = dist[row+1][col] + 1
            if dist[row+1][col] != 0:
                bottom = dist[row+1][col]

                   
        # left
        if col - 1 >= 0 and grid[row][col-1] == 1:
            if visited[row][col-1] == 0:
                visited[row][col-1] = 1
                if nearestTwo(grid,row,col-1,dist,visited) >= 1:
                    dist[row][col] = dist[row][col-1] + 1
            if dist[row][col-1] != 0:
                left = dist[row][col-1]

            
        # right
        if col + 1 < len(grid[row]) and grid[row][col+1] == 1:
            if visited[row][col+1] == 0:
                visited[row][col+1] = 1
                if nearestTwo(grid,row,col+1,dist,visited) >= 1:
                    dist[row][col] = dist[row][col+1] + 1
            if dist[row][col+1] != 0:
                right = dist[row][col+1]

        print(top,bottom,left,right)
        dist[row][col] = min(top,bottom,left,right)
        if dist[row][col] == max_minute or dist[row][col] == 0:
            dist[row][col] = 0
        else:
            dist[row][col] += 1
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
            if grid[row][col] == 1:
                # print("=============================")
                # print(row,col)
                # print("=============================")
                visited[row][col] = 1
                minute = nearestTwo(grid,row,col,dist,visited)
                # clean visited
                for i in range(len(visited)):
                    vrow = visited[i]
                    for j in range(len(vrow)):
                        vrow[j] = 0
                if minute != -1:
                    max_step = max(minute,max_step)
                else:
                    return -1
                
                # print()
    for row in range(len(dist)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1 and dist[row][col] == 0:
                return -1

    return max_step

grid = [[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]
# grid = [[1,1,1],[1,0,1],[1,0,2]]
grid = [[2],[2],[1],[0],[1],[1]]
print(orangesRotting(grid))
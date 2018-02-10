room = [['+' for x in range(10)] for y in range(10)]

def drawRect(grid, x1, y1, x2, y2 wall = '+', mid = ' '):
    if (0 < y1 < len(grid)) and (0 < y2 < len(grid) and (0 < x1 < len(grid[y])) and (0 < x2 < len(grid[y])):
        if y1 < y2:
            pass



def printGrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            print(grid[x][y], end='')
        print('')

printGrid(room)

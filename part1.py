from random import sample
from time import sleep



def printGrid(grid, x = False):
    
    if grid == None: return
    
    colors = ['','\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m', '\033[4m', '\033[1m']
    end = '\033[0m'

    print()
    print(" ___________ ")
    for i in range(0,9,3):
        if (i != 0): print('|___⊥___⊥___|')
        print( "| " + colors[grid[i]]   + (str(grid[i])   if grid[i]   != 0 else ' ') + end + 
              " | " + colors[grid[i+1]] + (str(grid[i+1]) if grid[i+1] != 0 else ' ') + end +
              " | " + colors[grid[i+2]] + (str(grid[i+2]) if grid[i+2] != 0 else ' ') + end +
              " |")

    print('⌞___⊥___⊥___⌟')

    if x: print("\033[%d;%dH" % (0,0))

def moveUp(grid):
    if grid == None: return None

    empty = [i for i in grid if grid[i] == 0][0] #The position of the empty slot
    if empty in [0,1,2]: return None
    
    grid[empty],grid[empty-3] = grid[empty-3], grid[empty]
    empty -= 3;
    return grid

def moveDown(grid):
    if grid == None: return None
    empty = [i for i in grid if grid[i] == 0][0] #The position of the empty slot
    if empty in [6,7,8]: return None

    grid[empty],grid[empty+3] = grid[empty+3], grid[empty]
    empty += 3
    return grid

def moveLeft(grid):
    if grid == None: return None
    empty = [i for i in grid if grid[i] == 0][0] #The position of the empty slot
    if empty in [0,3,6]: return None

    grid[empty],grid[empty-1] = grid[empty-1], grid[empty]
    empty -= 1
    return grid

def moveRight(grid):
    if grid == None: return None
    empty = [i for i in grid if grid[i] == 0][0] #The position of the empty slot
    if empty in [2,5,8]: return None

    grid[empty], grid[empty+1] = grid[empty+1], grid[empty]
    empty += 1
    return grid

win = lambda grid: grid == [1,2,3,4,5,6,7,8,0]

def bfs(grid):
    #From the current board configuration, take all possible moves (max 4) and check if it is the goal state
    pass

def main():
    #Grid data Structure. Initial Starting Grid is Randomised. 0 means the square is empty
    # grid = sample(range(9),9)
    grid = [5,8,7,6,0,4,3,2,1]
    
    while not win(grid):
        
        dt = 0.75

        grid = moveUp(grid)
        printGrid(grid, True)
        sleep(dt)

        grid = moveRight(grid)
        printGrid(grid, True)
        sleep(dt)

        grid = moveDown(grid)
        printGrid(grid, True)
        sleep(dt)

        grid = moveLeft(grid)
        printGrid(grid, True)
        sleep(dt)






if __name__ == "__main__":
    main()
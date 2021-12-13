from random import sample
from time import sleep

#Grid data Structure. Initial Starting Grid is Randomised. 0 means the square is empty
grid = sample(range(9),9)
empty = [i for i in grid if grid[i] == 0][0] #The position of the empty slot

def printGrid(x = False):
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

def moveUp():
    global empty
    if empty in [0,1,2]: return -1
    
    grid[empty],grid[empty-3] = grid[empty-3], grid[empty]
    empty -= 3;
    return 1;

def moveDown():
    global empty
    if empty in [6,7,8]: return -1

    grid[empty],grid[empty+3] = grid[empty+3], grid[empty]
    empty += 3
    return 1

def moveLeft():
    global empty
    if empty in [0,3,6]: return -1

    grid[empty],grid[empty-1] = grid[empty-1], grid[empty]
    empty -= 1
    return 1

def moveRight():
    global empty
    if empty in [2,5,8]: return -1

    grid[empty], grid[empty+1] = grid[empty+1], grid[empty]
    empty += 1
    return 1

win = lambda: grid == [1,2,3,4,5,6,7,8,0]

while True:

    dt = 0.75

    moveUp()
    printGrid(True)
    sleep(dt)

    moveRight()
    printGrid(True)
    sleep(dt)

    moveDown()
    printGrid(True)
    sleep(dt)

    moveLeft()
    printGrid(True)
    sleep(dt)

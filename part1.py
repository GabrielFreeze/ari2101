import random
import time
from copy import deepcopy


def printGrid(grid, x = False):
    
    if grid == None: return
    if x: print("\033[%d;%dH" % (0,0))
    
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

    

def moveUp(grid):
    if grid == None: return None
    new_grid = deepcopy(grid)

    empty = [i for i in new_grid if new_grid[i] == 0][0] #The position of the empty slot
    if empty in [0,1,2]: return None
    
    new_grid[empty],new_grid[empty-3] = new_grid[empty-3], new_grid[empty]
    return new_grid

def moveDown(grid):
    if grid == None: return None
    new_grid = deepcopy(grid)

    empty = [i for i in new_grid if new_grid[i] == 0][0] #The position of the empty slot
    if empty in [6,7,8]: return None

    new_grid[empty],new_grid[empty+3] = new_grid[empty+3], new_grid[empty]
    return new_grid

def moveLeft(grid):
    if grid == None: return None
    new_grid = deepcopy(grid)

    empty = [i for i in new_grid if new_grid[i] == 0][0] #The position of the empty slot
    if empty in [0,3,6]: return None

    new_grid[empty],new_grid[empty-1] = new_grid[empty-1], new_grid[empty]
    return new_grid

def moveRight(grid):
    if grid == None: return None
    new_grid = deepcopy(grid)

    empty = [i for i in new_grid if new_grid[i] == 0][0] #The position of the empty slot
    if empty in [2,5,8]: return None

    new_grid[empty], new_grid[empty+1] = new_grid[empty+1], new_grid[empty]
    return new_grid

win = lambda grid: grid == [1,2,3,4,5,6,7,8,0]

#One liner obfuscated function
# heuristic = lambda g,x=1:sum(x*(abs(i%3-((not t)*(((t-1)%(1<<3))+1)+(not not t)*(t-1))%3)+abs(i//3-([8,0,1,2,3,4,5,6,7][t])//3))+(not(x|((not t)*(((t-1)%8)+1)+(t&(not not ord("Gabriel_Freeze"[2+0+2+1])))*(t-1))-i)) for i,t in enumerate(g) if t)

def heuristic(grid,x = True):
    t = [8,0,1,2,3,4,5,6,7]
    w = 3

    if x: #Manhattan Distance
        return sum(abs(i%w - t[tile]%w) + abs(i//w - t[tile]//w) for i,tile in enumerate(grid) if tile != 0)
    else: #Number of Misplaced Tiles
        return sum(t[tile] == i for i,tile in enumerate(grid) if tile != 0)

def bfs(grid):
    # 0: UP
    # 1: DOWN
    # 2: RIGHT
    # 3: LEFT

    #Add the initial starting state
    #[i,j,s]
    # i = index of parent state
    # j = type of move (up,down,left,right)
    # s = the current grid configuration
    queue = [(-1,-1,grid)]

    #The index of the last added state in the queue
    parent_index = len(queue)-1

    diff = 0

    #Expanded intial grid
    for i,s in enumerate([moveUp(grid), moveDown(grid), moveRight(grid), moveLeft(grid)]):
        if s is not None:
            queue.append((0,i,s))
        if win(s):
            return [i]
    
    while True:
        
        #The index of the last added state
        diff += len(queue) - parent_index

        #The index of the last added parent state
        parent_index2 = len(queue)-1

        #Iterate through all the new states
        for i in range(parent_index+1,diff):

            #For every state, take the 4 possible moves to generate at most 4 new states
            for j,s in enumerate([moveUp(queue[i][2]), moveDown(queue[i][2]), moveRight(queue[i][2]), moveLeft(queue[i][2])]):
                
                #If the new state is unique and action is not opposite of parent, add it to the queue.
                if s is not None and (i,j,s) not in queue and [1,0,3,2][j] != queue[i][1]: 
                    queue.append((i,j,s))
                
                #If the state is a winning state, traverse back to the root node
                #by iteratively jumping to the current state's parent.
                if win(s):
                    path = [j]
                    k = i
                    
                    while k != 0:
                        path.insert(0,queue[k][1])
                        k = queue[k][0]
                    
                    return path
                
        #Update the index of the last added parent state.
        parent_index = parent_index2

def greedy_best(grid,x = True, visited=[]):
    #Initial state is added to the queue
    queue = [(-1,-1,grid,heuristic(grid,x))]
    visited = []
    node = []

    if win(grid): return []

    while queue:
        
        best = float('inf')

        #Get element with lowest
        for elem in queue:
            if elem[3] < best: 
                parent = elem[0]
                move = elem[1]
                node = elem[2]
                best = elem[3]
        
        queue.remove((parent,move,node,best))
        visited.append((parent,move,node))
        # print([i[2] for i in visited])
        
        #Expand node
        for i,s in enumerate([moveUp(node), moveDown(node), moveRight(node), moveLeft(node)]):
            
            if s is not None and (len(visited)-1,i,s) not in visited:
                
                if win(s):
                    
                    path = [i]
                    j,k,_ = visited[-1]
                    
                    while j != -1:
                        path.insert(0,k)
                        j,k,_ = visited[j]

                    return path
                    
                else:
                    queue.append((len(visited)-1,i,s,heuristic(s,x)))
        
        




def main():
    #Grid data Structure. Initial Starting Grid is Randomised. 0 means the square is empty
    
    grid = [1,2,3,4,5,6,7,8,0]

    # Shuffle grid by atmost 10 times
    for i in [int(random.random()*4) for _ in range(40)]:
        if   i == 0 and moveUp(grid)    is not None: grid = moveUp(grid) 
        elif i == 1 and moveDown(grid)  is not None: grid = moveDown(grid)
        elif i == 2 and moveRight(grid) is not None: grid = moveRight(grid)
        elif i == 3 and moveLeft(grid)  is not None: grid = moveLeft(grid)

    printGrid(grid)

    start = time.time()

    path = bfs(grid)
    
    print("Path found in " + str(time.time() - start))
    print([['UP','DOWN','RIGHT','LEFT'][i] for i in path])
    
    time.sleep(2.5)
    printGrid(grid,True)

    for i in path:
        if   i == 0: grid = moveUp(grid) 
        elif i == 1: grid = moveDown(grid)
        elif i == 2: grid = moveRight(grid)
        elif i == 3: grid = moveLeft(grid)

        printGrid(grid,True)
        time.sleep(1)


if __name__ == "__main__":
    main()
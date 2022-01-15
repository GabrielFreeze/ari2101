import random
import time
from copy import deepcopy
from os import sys


def printGridAnim(grid, x = False):
    
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
def printGrid(grid):
    
    if grid == None: return

    print(" ___________ ")
    for i in range(0,9,3):
        if (i != 0): print('|___|___|___|')
        print( "| " + (str(grid[i])   if grid[i]   != 0 else ' ') + 
              " | " + (str(grid[i+1]) if grid[i+1] != 0 else ' ') +
              " | " + (str(grid[i+2]) if grid[i+2] != 0 else ' ') +
              " |")

    print('|___|___|___|')


def printMenuColor():
    print("\t\033[91mChoose search strategy\033[0m\n")
    print("\033[92m[1]\033[0m\tBreadth First Search")
    print("\033[92m[2]\033[0m\tGreedy Best First Search")
    print("\033[92m[3]\033[0m\tA* Search")
    print("\033[92m[4]\033[0m\tEnforced Hill Climbing")

    search_option = 0

    while not (1 <= search_option <= 4):
        search_option = int(input('Option: '))

    if search_option != 1:
        print("\t\033[91mChoose heuristic\033[0m\n")
        print("\033[92m[1]\033[0m\t Number of Misplaced Tiles")
        print("\033[92m[2]\033[0m\t Manhattan Distance")

        heuristic_option = 0
        
        while not (1 <= heuristic_option <= 2):
            heuristic_option = int(input('Option: '))

    print("\t\033[91mEnter grid:\033[0m\n")
    grid_str = input("\033[92mExample [0,1,2,3,4,5,6,7,8]:\033[0m")

    if  grid_str[0] != '[' or grid_str[-1] != ']' or len(grid_str) != 19:
        sys.exit("Invalid Grid Coniguration")
    
    grid = []

    for i in grid_str[1:-1].split(','):
        j = int(i)
        if j in grid or j < 0 or j > 8:
            sys.exit("Invalid Grid Coniguration")
        
        grid.append(int(i))
    
    return search_option,heuristic_option,grid

    
    
def printMenu():
    
    search_option    = 0
    heuristic_option = -1

    print("\tChoose search strategy\n")
    print("[1]\tBreadth First Search")
    print("[2]\tGreedy Best First Search")
    print("[3]\tA* Search")
    print("[4]\tEnforced Hill Climbing")


    while not (1 <= search_option <= 4):
        search_option = int(input('Option: '))

    if search_option != 1:
        print("\tChoose heuristic\n")
        print("[1]\t Number of Misplaced Tiles")
        print("[2]\t Manhattan Distance")

        heuristic_option = 0
        
        while not (1 <= heuristic_option <= 2):
            heuristic_option = int(input('Option: '))
    
    
    print("\tEnter grid:\n")
    grid_str = input("Example: [0,1,2,3,4,5,6,7,8]: \n")

    if (grid_str[0] != '[' or grid_str[-1] != ']' or len(grid_str) != 19):
        sys.exit("Invalid Grid Coniguration")
    grid = []


    for i in grid_str[1:-1].split(','):
        j = int(i)
        if j in grid or j < 0 or j > 8: sys.exit("Invalid Grid Coniguration")
        grid.append(int(i)) 

    return search_option,heuristic_option,grid
    


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

def cost(start, end = [1,2,3,4,5,6,7,8,0], x = True):
    #A starting configuration
    #B final configuration. GOAL CONFIGURATION

    A = [(i,j) for i,j in enumerate(end)]
    A.sort(key=lambda x: x[1])

    t = [i for i,_ in A]
    
    w = 3

    if x: #Manhattan Distance
        return sum(abs(i%w - t[tile]%w) + abs(i//w - t[tile]//w) for i,tile in enumerate(start) if tile != 0)
    else: #Number of Misplaced Tiles
        return sum(t[tile] == i for i,tile in enumerate(start) if tile != 0)
def heuristic(grid, x = True):
    
    
    t = [8,0,1,2,3,4,5,6,7]
    w = 3

    if x: #Manhattan Distance
        return sum(abs(i%w - t[tile]%w) + abs(i//w - t[tile]//w) for i,tile in enumerate(grid) if tile != 0)
    else: #Number of Misplaced Tiles
        return sum(t[tile] != i for i,tile in enumerate(grid) if tile != 0)

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
    start = time.time()

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
        
        if (time.time() - start > 900):
            return 900,0,[]

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
                    end = time.time() - start
                    path = [j]
                    k = i
                    
                    while k != 0:
                        path.insert(0,queue[k][1])
                        k = queue[k][0]
                    
                    return end,len(queue),path
                
        #Update the index of the last added parent state.
        parent_index = parent_index2
def greedy_best(grid,x = True):
    
    start = time.time()

    #Initial state is added to the queue
    queue = [(-1,-1,grid,heuristic(grid,x))]
    visited = []
    node = []

    if win(grid): return 0,[]

    while queue:
        
        if (time.time() - start > 900):
            return 900,0,[]

        best = float('inf')

        #Get element with lowest heuristic (h(n))
        for elem in queue:
            if elem[3] < best: 
                parent = elem[0]
                move = elem[1]
                node = elem[2]
                best = elem[3]
        
        #Remove element from open queue, add to visited list.
        queue.remove((parent,move,node,best))
        visited.append((parent,move,node))
        
        #Expand node
        for i,s in enumerate([moveUp(node), moveDown(node), moveRight(node), moveLeft(node)]):
            
            if s is not None and (len(visited)-1,i,s) not in visited and [1,0,3,2][i] != move:
                #If a child state is a goal state then get parent states and return list of their moves
                if win(s):
                    end = time.time() - start
                    path = [i]
                    j,k,_ = visited[-1]
                    
                    while j != -1:
                        path.insert(0,k)
                        j,k,_ = visited[j]
                  
                    return end,len(visited)+len(queue),path
                
                #Otherwise append the child state to the open queue, alongside its heuristic value.
                else:
                    queue.append((len(visited)-1, i, s, heuristic(s,x)))
def a_star(grid,x = True):
    
    start = time.time()

    #Initial state is added to the queue
    queue = [(-1,-1,grid,heuristic(grid,x),0)]
    visited = []
    node = []
    if win(grid): return []

    while queue:
        
        if (time.time() - start > 900):
            return 900,0,[]

        best = float('inf')

        #Get element with lowest cost (g(n) + h(n))
        for elem in queue:
            if elem[3] < best: 
                parent = elem[0]
                move = elem[1]
                node = elem[2]
                best = elem[3]
                parent_cost = elem[4]
        
        queue.remove((parent,move,node,best,parent_cost))
        visited.append((parent,move,node))
        
        #Expand node
        for i,s in enumerate([moveUp(node), moveDown(node), moveRight(node), moveLeft(node)]):
            
            if s is not None and (len(visited)-1,i,s) not in visited and [1,0,3,2][i] != move:
                if win(s):
                    end = time.time() - start
                    path = [i]
                    j,k,_ = visited[-1]
                    
                    while j != -1:
                        path.insert(0,k)
                        j,k,_ = visited[j]
                    return end,len(queue)+len(visited),path
                    
                else:
                    queue.append((len(visited)-1, i, s, parent_cost+1+heuristic(s,x),parent_cost+1))
def ehc(grid, x = True):
    
    start = time.time()

    if win(grid): return []

    queue = [(-1,-1,grid)]
    best = heuristic(grid,x)
    visited = []

    while queue:

        if (time.time() - start > 900):
            return 900,0,[]

        node = queue.pop(0)
        visited.append(node)

        parent = node[0]
        move   = node[1]
        grid   = node[2]
        

        for i,s in enumerate([moveUp(grid), moveDown(grid), moveRight(grid), moveLeft(grid)]):        
      
            if s is not None and (len(visited)-1,i,s) not in visited and [1,0,3,2][i] != move:

                if win(s):
                    end = time.time() - start
                    path = [i]
                    j,k,_ = visited[-1]
                    
                    while j != -1:
                        path.insert(0,k)
                        j,k,_ = visited[j]

                    return end,len(queue)+len(visited),path

                queue.append((len(visited)-1,i,s))
                h = heuristic(s,x)

                if h < best:
                    queue = []
                    best = h
                    queue.append((len(visited)-1,i,s))
                    break
             

def main():
    a,b,grid = printMenu()
    

    printGrid(grid)


    if a == 1: elapsed,states,path = bfs(grid)
    if a == 2: elapsed,states,path = greedy_best(grid, b-1)
    if a == 3: elapsed,states,path = a_star(grid, b-1)
    if a == 4: elapsed,states,path = ehc(grid, b-1)
    

    print("Time taken: " + str(round(elapsed,3)))
    print("Length of plan: " + str(len(path)))
    print("Unique states expanded: " + str(states))
    if elapsed == 900: print('Validitiy: NOT VALID\n')
    else:              print('Validitiy: VALID\n')
    print([['UP','DOWN','RIGHT','LEFT'][i] for i in path])
    
    time.sleep(2.5)
    
    
    printGrid(grid)

    for i in path:
        if i == 0: grid = moveUp(grid) 
        if i == 1: grid = moveDown(grid)
        if i == 2: grid = moveRight(grid)
        if i == 3: grid = moveLeft(grid)
        
        printGrid(grid)

        time.sleep(1)


if __name__ == "__main__":
    main()

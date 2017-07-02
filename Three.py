'''
Created on Jun 29, 2017

@author: rjw0028
'''
import time, sys
sys.setrecursionlimit(2000)
MIN_ZEROS = 10

_SOLVED_ = False
_SUDOKU_ =  [[4,0,8,0,0,2,0,0,0],
             [0,6,0,0,8,0,0,2,0],
             [0,0,0,3,0,0,1,0,4],
             [0,0,4,8,3,0,0,1,0],
             [1,0,0,0,0,0,0,3,8],
             [0,0,2,4,0,0,5,0,0],
             [0,0,3,0,0,1,9,0,0],
             [6,4,0,0,0,0,0,0,1],
             [0,7,0,0,9,8,6,0,0]]# Any SUDOKU puzzle



_SUDOKU_1 = [[0,0,0,0,0,5,0,8,0],[0,0,0,6,0,1,0,4,3],[0,0,0,0,0,0,0,0,0],[0,1,0,5,0,0,0,0,0],[0,0,0,1,0,6,0,0,0],[3,0,0,0,0,0,0,0,5],[5,3,0,0,0,0,0,6,1],[0,0,0,0,0,0,0,0,4],[0,0,0,0,0,0,0,0,0]]


All_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
C = 0
D = 0
Cells = [[[] for y in range(9)] for x in range(9)] # Will contain all info about each cell

def isSolved(puzzle):   # Checks if there is a 0 in the puzzle. If not, declares as solved.
    res = True
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                res = False
                break
        else:
            continue
        break
    return res
def cellOptions(i, j, puzzle):  # Creates and returns a list of options that can be fit in a given cell...
    List = []
    for x in range(9):
        if ((x != j) and puzzle[i][x] != 0) :
            List.append(puzzle[i][x])
    for x in range(9):
        if ((x != i) or puzzle[x][j] != 0) :
            List.append(puzzle[x][j])
    
    ix = int((i)/3)
    iy = int((j)/3)
    #print "iy: ", iy
    for x in range(3*ix, 3*ix + 3):
        for y in range(3*iy, 3*iy + 3):
            if not (x==i and y==j):
                if (puzzle[x][j] != 0):
                    #print x, y
                    List.append(puzzle[x][y])
    v = set(List)
    values = []
    val = []
    for x in v:
        val.append(x)        
    
    for y in All_digits:
        if y not in val:
            values.append(y)
    return values
def printPuzzle(puzzle):    # prints any given matrix by row...
    for i in puzzle:
        print i     
def fillCells(puzzle):      # Function that creates a 2D matrix that maintains all the options there are for a cell...
    r = [[[] for y in range(9)] for x in range(9)]
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                r[i][j] = cellOptions(i, j, puzzle)
            else:
                r[i][j] = []
#     for t in r:
#         print t 
    return r

def updatePuzzle(puzzle, cel):
    for i in range(9):
        for j in range(9):
            if len(cel[i][j]) == 1:
                puzzle[i][j] = cel[i][j][0]
    return puzzle

    
def Solution2(puzzle):
    global _SOLVED_
    x = 10
    y = 10
    #if (C%1 == 0 or (C-1)%1 == 0):
        #printPuzzle(puzzle)
    if isSolved(puzzle):
        print "The Puzzle is Solved..."
        printPuzzle(puzzle)
        _SOLVED_ = True
        return
    
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                x = i
                y = j
                break
        else:
            continue
        break
    
    Opts = cellOptions(x, y, puzzle)
    for i in range(len(Opts)):
        puzzle[x][y] = Opts[i]
        Solution2(puzzle)
        if _SOLVED_:
            return
    puzzle[x][y] = 0

def Solution1(puzzle):
    global C        # Counting number of iterations
    #printPuzzle(puzzle)
    if isSolved(puzzle):
        print "The Puzzle is Solved..."
        printPuzzle(puzzle)
        return [puzzle, 1] 
    else:
        Done = True
        while(Done):
            Copy_Cells1 = fillCells(puzzle)
            #print "Puzzle: "
            puzzle = updatePuzzle(puzzle, Copy_Cells1)
            #printPuzzle(puzzle)
            #print "Cells 2 : "
            Copy_Cells2 = fillCells(puzzle)
            #print "Compared: ", cmp(Copy_Cells1, Copy_Cells2)
            if Copy_Cells1 == Copy_Cells2:
                return [puzzle, 0]
    
def main():
    start_time = time.time()
    global Cells
    
    print "Hello Sudoku"
    puzzle = _SUDOKU_
    printPuzzle(_SUDOKU_)
    
    puzzle = Solution1(puzzle)[0]
    result = Solution1(puzzle)[1]
    
    if result == 0:
        Solution2(puzzle)
    elapsed_time = time.time() - start_time
    print elapsed_time
    

if __name__ == "__main__":   
    main()
"""
Sample Board
[
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
Rules of Sudoku:
3x3 squares no duplicates
Rows and Columns no duplicates

Solution Algorithm: Backtracking
"""
import pprint as pp

def solve(board):
    br = board

    # Input a Row Number (y) and the Number (num) being compared to the row
    def checkRow(y,num):
        if num in br[y]:
            return False
        return True
    
    # Input a Column Number (x) and the Number (num) being compared to the column
    def checkCol(x, num):
        if num in [br[y][x] for y in range(9)]:
            return False
        return True
    
    # Input Position of Value to be Inserted (x = Column, y = Row) and Number (num) being compared to the 3x3
    def check3(x, y, num): 
        # 3 Options (y + 1) % 3 = 0,1,2. 1 -> Pos(y) Top of 3x3, 2 -> Pos(y) Middle of 3x3, 0  -> Pos(y) Bottom of 3x3
        
        # 3 Options (x + 1) % 3 = 0,1,2. 1 -> Pos(x) Left of 3x3, 2 -> Pos(x) Middle of 3x3, 0 -> Pos(x) Right of 3x3

        # Helper function X = (x+1) % 3, Y = (y+1) % 3. Used to figure out what squares around the value to check
        def helper(x,y):
            X = (x+1) % 3
            Y = (y+1) % 3
            
            if X == 1:
                if Y == 1:
                    return [br[y][x:x+3] for y in range(y,y+3)]
                if Y == 2:
                    return [br[y][x:x+3] for y in range(y-1,y+2)]
                return [br[y][x:x+3] for y in range(y-2,y+1)]

            if X == 2:
                if Y == 1:
                    return [br[y][x-1:x+2] for y in range(y,y+3)]
                if Y == 2:
                    return [br[y][x-1:x+2] for y in range(y-1,y+2)]
                return [br[y][x-1:x+2] for y in range(y-2,y+1)]

            if Y == 1:
                return [br[y][x-2:x+1] for y in range(y,y+3)]
            if Y == 2:
                return [br[y][x-2:x+1] for y in range(y-1,y+2)]
            return [br[y][x-2:x+1] for y in range(y-2,y+1)]

        square = helper(x,y)
        for x in range(3):
            if num in square[x]:
                return False
        return True

    # Returns True if adding the number follows all rules.
    def fulltest(x,y,num):
        return check3(x,y,num) and checkCol(x,num) and checkRow(y,num)
    

    # Backtracking Algo
    def solveHelper(x,y):

        # Base Case: if Y is equal to 9 it is out of bounds and the algorithim succeeded
        if y == 9:
            return True
        
        # If X is equal to 9 the algorithim needs to move down a row
        if x == 9:
            if(solveHelper(0,y+1)):
                return True
            return False

        # Move on if one of the numbers are already set initially
        if br[y][x] != 0:
            if(solveHelper(x+1,y)):
                return True
            return False
        
        # Exaust 1-9 for each cell before moving down the row
        for i in range(1,10):
            #print(f"X = {x}, Y = {y}, I = {i}")
            if(fulltest(x,y,i)):
                br[y][x] = i
                if(solveHelper(x+1,y)):
                    return True
        br[y][x] = 0
        return False
    
    if(solveHelper(0,0)):
        return br
    return "Cannot be Completed"


                

        











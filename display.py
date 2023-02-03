import pygame as pg
import sudokuSolve as s
import copy as c

board = [
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

# Just making a copy to check whether number was already part of the puzzle 
# Made these Deepcopies so that operations done / changes made on one will not affect the other
boardCheck = c.deepcopy(board) 
solved = s.solve(c.deepcopy(board))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (62,128,11)
RED = (145,37,25)
LIGHT_BLUE = (88,196,213)

pg.init()

font1 = pg.font.SysFont('chalkduster.ttf', 24)
solveButton = font1.render("Solve", True, BLACK)
checkButton = font1.render("Check", True, BLACK)
leftArrow = font1.render("<", True, BLACK)
rightArrow = font1.render(">", True, BLACK)


canvas = pg.display.set_mode((1200,900))

pg.display.set_caption("Sudoku Solver")
exit = False
active = (-1,-1) # active(x,y) is the spot on the board that will receive the number, if -1,-1 that means no spot is active
checkActive = False # if the check is True, different colors will be used for the numbers to signify whether it is right or wrong
keysAllowed = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9] # the only keys users should be allowed to use

# Main Game Loop
while not exit:
    mousePOS = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True

        # Checking for mouse click on cell
        if event.type == pg.MOUSEBUTTONUP:
            #mousePOS = pg.mouse.get_pos()
            if mousePOS[0] < 900: # Is it on the board
                x = mousePOS[0] // 100
                y = mousePOS[1] // 100
                #print(f"X: {x}, Y: {y}, Value: {br[y][x]}") <- Testing
                if boardCheck[y][x] == 0:
                    active = (x,y)
            else: # If in the button area
                # Solve Button
                if 998 <= mousePOS[0] <= 1102 and 423 <= mousePOS[1] <= 477:
                    board = solved
                # Check Button
                if 998 <= mousePOS[0] <= 1102 and 358 <= mousePOS[1] <= 402:
                    checkActive = not checkActive
                
        
        # As long as there is an active cell a number can be typed
        if event.type == pg.KEYDOWN:
            if event.key in keysAllowed and active != (-1,-1): # No out of bounds error because of this check
                board[active[1]][active[0]] = event.unicode
                active = (-1,-1)
    
    canvas.fill(WHITE)

    # Drawing buttons
    # Button 1 - Solve
    pg.draw.rect(canvas, BLACK, [998,423,104,54])
    if 998 <= mousePOS[0] <= 1102 and 423 <= mousePOS[1] <= 477:
        pg.draw.rect(canvas, LIGHT_BLUE, [1002,427,96,46])
    else:
        pg.draw.rect(canvas, WHITE, [1002,427,96,46])
    canvas.blit(solveButton, (1028,445))

    # Button 2 - Check
    pg.draw.rect(canvas, BLACK, [998,348,104,54])
    if 998 <= mousePOS[0] <= 1102 and 348 <= mousePOS[1] <= 402:
        pg.draw.rect(canvas, LIGHT_BLUE, [1002,352,96,46])
    else:
        pg.draw.rect(canvas, WHITE, [1002,352,96,46])
    canvas.blit(checkButton, (1027,370))

    # Button 3 - Change Board? TBD
    pg.draw.rect(canvas, BLACK, [998,498,104,54])
    if 998 <= mousePOS[0] < 1050 and 498 <= mousePOS[1] <= 552:
        pg.draw.rect(canvas, LIGHT_BLUE, [1002,502,48,46])
    else:
        pg.draw.rect(canvas, WHITE, [1002,502,48,46])
    if 1050 < mousePOS[0] < 1102 and 498 <= mousePOS[1] <= 552:
        pg.draw.rect(canvas, LIGHT_BLUE, [1050,502,48,46])
    else:
        pg.draw.rect(canvas, WHITE, [1050,502,48,46])
    pg.draw.line(canvas, BLACK, (1050,498),(1050,551),3)
    canvas.blit(leftArrow, (1019,517))
    canvas.blit(rightArrow, (1072,517))

    # Drawing the board
    for x in range(10):
        if x % 3 != 0:
            pg.draw.line(canvas,BLACK, ((x*100),0),((x*100),900))
            pg.draw.line(canvas,BLACK, (0,(x*100)),(900,(x*100)))
        else:
            pg.draw.line(canvas,BLACK, ((x*100),0),((x*100),900),3)
            pg.draw.line(canvas,BLACK, (0,(x*100)),(900,(x*100)),3)
    
    # Adding the numbers
    for y in range(9):
        for x in range(9):
            if board[y][x] != 0:
                if checkActive:
                    if board[y][x] == solved[y][x]:
                        num = font1.render(str(board[y][x]), True, GREEN)
                        canvas.blit(num,((x*100)+45,(y*100+45)))
                    else:
                        num = font1.render(str(board[y][x]), True, RED)
                        canvas.blit(num,((x*100)+45,(y*100+45)))
                else:    
                    num = font1.render(str(board[y][x]), True, BLACK)
                    canvas.blit(num,((x*100)+45,(y*100+45)))
    
    pg.display.update()
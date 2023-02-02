import pygame as pg
import sudokuSolve as s

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

#Just making a copy to check whether number was already part of the puzzle
boardCheck = board

WHITE = (255,255,255)
BLACK = (0,0,0)

pg.init()

font1 = pg.font.SysFont('chalkduster.ttf', 18)
solveButton = font1.render("Solve", True, BLACK)


canvas = pg.display.set_mode((1200,900))

pg.display.set_caption("Sudoku Solver")
exit = False
active = (-1,-1) # active(x,y) is the spot on the board that will receive the number, if -1,-1 that means no spot is active
keysAllowed = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9] # the only keys users should be allowed to use

# Main Game Loop
while not exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True

        # Checking for mouse click on cell
        if event.type == pg.MOUSEBUTTONUP:
            mousePOS = pg.mouse.get_pos()
            if mousePOS[0] < 900: # Is it on the board
                x = mousePOS[0] // 100
                y = mousePOS[1] // 100
                #print(f"X: {x}, Y: {y}, Value: {br[y][x]}") <- Testing
                if boardCheck[y][x] == 0:
                    active = (x,y)
            else: #If in the button area
                if 998 <= mousePOS[0] <= 1102 and 423 <= mousePOS[1] <= 477:
                    board = s.solve(boardCheck)
        
        # As long as there is an active cell a number can be typed
        if event.type == pg.KEYDOWN:
            if event.key in keysAllowed and active != (-1,-1): # No out of bounds error because of this check
                board[active[1]][active[0]] = event.unicode
                active = (-1,-1)
    
    canvas.fill(WHITE)

    # Drawing buttons
    pg.draw.rect(canvas, BLACK, [998,423,104,54])
    pg.draw.rect(canvas, WHITE, [1002,427,96,46])
    canvas.blit(solveButton,(1032,445))

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
                num = font1.render(str(board[y][x]), True, BLACK)
                canvas.blit(num,((x*100)+45,(y*100+45)))
    
    pg.display.update()
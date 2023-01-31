import pygame as pg
import sodokuSolve as s

br = [
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

WHITE = (255,255,255)
BLACK = (0,0,0)

pg.init()

font1 = pg.font.SysFont('chalkduster.ttf', 18)


canvas = pg.display.set_mode((900,900))

pg.display.set_caption("Sudoku Solver")
exit = False

while not exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True
    
    canvas.fill(WHITE)
    for x in range(9):
        if x % 3 != 0:
            pg.draw.line(canvas,BLACK, ((x*100),0),((x*100),900))
            pg.draw.line(canvas,BLACK, (0,(x*100)),(900,(x*100)))
        else:
            pg.draw.line(canvas,BLACK, ((x*100),0),((x*100),900),3)
            pg.draw.line(canvas,BLACK, (0,(x*100)),(900,(x*100)),3)
    
    for x in range(9):
        for y in range(9):
            if br[x][y] != 0:
                num = font1.render(str(br[x][y]), True, BLACK)
                canvas.blit(num,((x*100)+45,(y*100+45)))

    #br = s.solve(br)
    
    
    pg.display.update()
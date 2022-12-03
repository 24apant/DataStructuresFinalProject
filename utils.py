import pygame
import classes

from settings import *
def drawCell(screen, color, row, cols):
    pygame.draw.circle(screen, color, [BUFFER_AROUND + (cols * CELL_SIZE + CELL_SIZE / 2),
                                       BUFFER_AROUND + (row * CELL_SIZE + CELL_SIZE / 2)],
                       CELL_SIZE / 2 - BUFFER_AROUND / 2)


def drawBoard(b, screen, activecol):
    board = b.contents
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                # player color
                drawCell(screen, (240, 230, 140), i, j)
            elif board[i][j] == -1:
                drawCell(screen, (255, 0, 0), i, j)
            elif j == activecol:
                drawCell(screen, (192, 192, 192), i, j)
            else:
                drawCell(screen, (51, 51, 51), i, j)

#covert board to b3
def convBoardToB3(board):
    if not isinstance(board, classes.Board):
        return
    contents = board.contents
    # add all contents into one array
    fullBoardArr = []
    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if contents[i][j] == -1:
                fullBoardArr.append(2)
            else:
                fullBoardArr.append(contents[i][j])
    #hash in base 3
    b3 = 0
    exponentMult = len(fullBoardArr) - 1
    for i in fullBoardArr:
        b3 += (3 ** exponentMult)*i
        exponentMult -= 1
    return b3



if __name__ == "__main__":
    test = classes.Board()
    testBoard = [
        [0,1],
        [2,1]
    ]
    test.setBoard(testBoard)
    print(convBoardToB3(test))
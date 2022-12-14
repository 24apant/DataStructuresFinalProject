import pygame
from funcs import classes

from settings import *


#Universal util functions

# Draws a cell at a row and column
def drawCell(screen, color, row, cols):
    pygame.draw.circle(screen, color, [BUFFER_AROUND + (cols * CELL_SIZE + CELL_SIZE / 2),
                                       BUFFER_AROUND + (row * CELL_SIZE + CELL_SIZE / 2)],
                       CELL_SIZE / 2 - BUFFER_AROUND / 2)

# Draw the entire board for a board 'b' the target gui, and the 'active' column aka the column which the player is
# hovering
def drawBoard(b, screen, activecol=None):
    board = b.contents
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                # player color
                drawCell(screen, (240, 230, 140), i, j)
            elif board[i][j] == -1:
                drawCell(screen, (255, 0, 0), i, j)
            elif activecol is not None and j == activecol:
                drawCell(screen, (192, 192, 192), i, j)
            else:
                drawCell(screen, (51, 51, 51), i, j)


# covert board to base 3
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
    # hash in base 3
    b3 = 0
    exponentMult = len(fullBoardArr) - 1
    for i in fullBoardArr:
        b3 += (3 ** exponentMult) * i
        exponentMult -= 1
    return b3

# Writes something on the bubble in trainer
def blitBubbleContent(message, font, gui, exit=False, hint=None):
    if exit:
        text = font.render("Press 'esc' to main menu", False, (200, 200, 200))
        newAnchor = (BUBBLE_TEXT_CONTENT_TL_ANCHOR[0], BUBBLE_TEXT_CONTENT_TL_ANCHOR[1] + (15 * TEXT_SIZE))
        gui.blit(text, newAnchor)

    else:
        btw = BUBBLE_TEXT_WRAP
        if hint is not None:
            newMsg = hint
            btw *= 2
        else:
            newMsg = message
        arr = [""]
        l = newMsg.split()
        # break message into smaller strs and store in arr
        counter = 0
        charCounter = 0
        for q in l:
            if charCounter + len(q) >= btw:
                charCounter = 0
                arr.append("")
                counter += 1
            arr[counter] += q + " "
            charCounter += len(q)

        for i in range(len(arr)):
            msg = arr[i]
            text = font.render(msg, False, (0, 0, 0))
            if hint is not None:
                text = font.render(msg, False, YELLOW_PLAYER_COLOR)
            newAnchor = (BUBBLE_TEXT_CONTENT_TL_ANCHOR[0], BUBBLE_TEXT_CONTENT_TL_ANCHOR[1] + (i * TEXT_SIZE))
            if hint is not None:
                gui.blit(text, (newAnchor[0], newAnchor[1] + 10 * BUFFER_AROUND))
            else:
                gui.blit(text, newAnchor)


# Tests
if __name__ == "__main__":
    test = classes.Board()
    testBoard = [
        [0, 1],
        [2, 1]
    ]
    test.setBoard(testBoard)
    print(convBoardToB3(test))

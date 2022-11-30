# connect 4 pygame
import sys

import minimax
from utils import *
import keyboard

game_over = False
frozen = False
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = pygame.time.Clock()
board = Board()
col_dims = []

for i in range(NUM_COLS):
    col_dims.append([BUFFER_AROUND + (CELL_SIZE * i), BUFFER_AROUND + (i * CELL_SIZE) + CELL_SIZE])
activeCol = -1
currPlayer = 1
AI_ENABLED = True
if AI_ENABLED:
    ai = minimax.minimaxAlgorithm(board, depth=4)
bg = (51, 51, 51)
while not game_over:
    screen.fill(bg)
    pygame.draw.rect(screen, (0, 0, 255), [BUFFER_AROUND, BUFFER_AROUND, GAME_WIDTH - BUFFER_AROUND - BUFFER_AROUND,
                                           GAME_HEIGHT - BUFFER_AROUND - BUFFER_AROUND])

    for event in pygame.event.get():
        mX, mY = pygame.mouse.get_pos()
        for i in range(NUM_COLS):
            if col_dims[i][0] < mX < col_dims[i][1]:
                activeCol = i
        if event.type == pygame.QUIT:
            sys.exit()
        if not frozen:
            if event.type == pygame.MOUSEBUTTONUP:
                # drop the piece all the way down col
                if board.checkForWinner() != 0:
                    frozen = True
                    if board.checkForWinner() == 1:
                        bg = YELLOW_PLAYER_COLOR
                        print("Winner")

                    elif board.checkForWinner() == 2:
                        bg = (255, 255, 255)
                        print("Tie")

                    else:
                        bg = (255, 0, 0)
                        print("Loser")

                if not frozen and board.addCell(activeCol, currPlayer):
                    currPlayer *= -1
                    if board.checkForWinner() != 0:
                        if board.checkForWinner() == 1:
                            bg = YELLOW_PLAYER_COLOR
                            print("Winner")

                        elif board.checkForWinner() == 2:
                            bg = (255, 255, 255)
                            print("Tie")

                        else:
                            bg = (255, 0, 0)
                            print("Loser")

                    if AI_ENABLED and not frozen and currPlayer == -1:
                        ai.updateBoard(board)
                        if board.isColFull(ai.getBestMoveFromTree()):
                            print("AI messed up")
                        if board.addCell(ai.getBestMoveFromTree(), currPlayer):
                            currPlayer *= -1
    if AI_ENABLED and not frozen and currPlayer == -1:
        ai.updateBoard(board)
        if board.addCell(ai.getBestMoveFromTree(), currPlayer):
            currPlayer *= -1
    if keyboard.is_pressed("p") and DEBUG_KEYBOARD_GET_BOARD_INPS:
        # prints board
        board.print()
    drawBoard(board, screen, activeCol)

    clock.tick(60)
    pygame.display.update()

# connect 4 main game against AI!
import sys

import pygame.math

from funcs.utils import *
import keyboard
from funcs import classes, minimax

game_over = False
frozen = False
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = pygame.time.Clock()
board = classes.Board()
col_dims = []
bg = BACKGROUND_COLOR  # background is dynamic

for i in range(NUM_COLS):
    col_dims.append([BUFFER_AROUND + (CELL_SIZE * i), BUFFER_AROUND + (i * CELL_SIZE) + CELL_SIZE])

activeCol = -1
currPlayer = 1
cTime = 0

AI_ENABLED = False
DOUBLE_AI = False
if AI_ENABLED:
    ai = minimax.minimaxAlgorithm(board, depth=AI_DEPTH)
if DOUBLE_AI:
    pAI = minimax.minimaxAlgorithm(board, depth=AI_DEPTH)
    randomWaitTime = -1

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
            if event.type == pygame.MOUSEBUTTONUP and not DOUBLE_AI:
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
                    drawBoard(board, screen, activeCol)
                    pygame.display.update()
                    if AI_ENABLED and not frozen and currPlayer == -1:
                        ai.updateBoard(board)
                        if ai.getBestMoveFromTreeAB() is not None and board.isColFull(ai.getBestMoveFromTreeAB()):
                            print("AI messed up")
                        if board.addCell(ai.getBestMoveFromTreeAB(), currPlayer):
                            currPlayer *= -1
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
    if AI_ENABLED and not frozen and currPlayer == -1:
        ai.updateBoard(board)
        if board.addCell(ai.getBestMoveFromTreeAB(), currPlayer):
            currPlayer *= -1
    if keyboard.is_pressed("p") and DEBUG_KEYBOARD_GET_BOARD_INPS:
        print(board.checkForWinner())
    if DOUBLE_AI:
        drawBoard(board, screen)
    else:
        drawBoard(board,screen,activeCol)
    if board.checkForWinner() == -1:
        pygame.display.set_caption("AI Wins!")
    else:
        pygame.display.set_caption("AI perceived score: " + str(board.evaluateBoard()))
    if DOUBLE_AI:
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
        pAI.updateBoard(board)
        if pAI.getBestMoveFromTreeAB() is not None and board.isColFull(pAI.getBestMoveFromTreeAB()):
            print("AI messed up")
        if not frozen and board.addCell(pAI.getBestMoveFromTreeAB(), currPlayer):
            currPlayer *= -1
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

    if AI_ENABLED and not frozen and currPlayer == -1 and DOUBLE_AI:
        ai.updateBoard(board)
        if ai.getBestMoveFromTreeAB() is not None and board.isColFull(ai.getBestMoveFromTreeAB()):
            print("AI messed up")
        if board.addCell(ai.getBestMoveFromTreeAB(), currPlayer):
            currPlayer *= -1
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
    clock.tick(100)
    pygame.display.update()

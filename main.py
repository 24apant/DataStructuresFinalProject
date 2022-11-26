# connect 4 pygame
import pygame
import sys
from settings import *
from utils import *
import minimax

game_over = False
frozen = False
screen = pygame.display.set_mode((GAME_SIZE, GAME_SIZE))
clock = pygame.time.Clock()
board = []
col_dims = []
for i in range(NUM_CELLS):
    board.append([])
    col_dims.append([BUFFER_AROUND + (CELL_SIZE * i), BUFFER_AROUND + (i * CELL_SIZE) + CELL_SIZE])
    for j in range(8):
        board[i].append(0)
activeCol = -1
currPlayer = 1
AI_ENABLED = False

while not game_over:
    screen.fill((51, 51, 51))

    pygame.draw.rect(screen, (0, 0, 255), [BUFFER_AROUND, BUFFER_AROUND, GAME_SIZE - BUFFER_AROUND - BUFFER_AROUND,
                                           GAME_SIZE - BUFFER_AROUND - BUFFER_AROUND])
    for event in pygame.event.get():
        mX, mY = pygame.mouse.get_pos()
        for i in range(NUM_CELLS):
            if col_dims[i][0] < mX < col_dims[i][1]:
                activeCol = i
        if event.type == pygame.QUIT:
            sys.exit()
        if not frozen:
            if event.type == pygame.MOUSEBUTTONUP:
                # drop the piece all the way down col
                if checkForWinner(board) != 0:
                    print("Winner")
                    frozen = True

                if not frozen and insertCellIntoBoard(board, activeCol, currPlayer):
                    currPlayer *= -1

    drawBoard(board, screen, activeCol)

    clock.tick(60)
    pygame.display.update()

import pygame
from settings import *


def drawCell(screen, color, row, cols):
    pygame.draw.circle(screen, color, [BUFFER_AROUND + (cols * CELL_SIZE + CELL_SIZE / 2),
                                       BUFFER_AROUND + (row * CELL_SIZE + CELL_SIZE / 2)],
                       CELL_SIZE / 2 - BUFFER_AROUND / 2)


def drawBoard(board, screen, activecol):
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


def checkForWinner(board):
    # check all vertical 4's
    possWinners = [1, -1]
    for i in range(NUM_CELLS - 4 + 1):
        for j in range(NUM_CELLS):
            for k in possWinners:
                if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == k:
                    return k
                    # check all horizontal 4's
    for i in range(NUM_CELLS):
        for j in range(NUM_CELLS - 4 + 1):
            for k in possWinners:
                if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == k:
                    return k
    # check all TRBL 4's
    for i in range(int(NUM_CELLS / 2) + 1):
        for j in range(int(NUM_CELLS / 2 - 1), NUM_CELLS):
            for k in possWinners:
                if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3] == k:
                    return k
    # check all TLBR 4s
    for i in range(0, int(NUM_CELLS / 2) + 1):
        for j in range(0, int(NUM_CELLS / 2) + 1):
            for k in possWinners:
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == k:
                    return k
    return 0


def insertCellIntoBoard(boardz, column, playerId):
    for i in range(NUM_CELLS - 1, -1, -1):
        if boardz[i][column] == 0:
            boardz[i][column] = playerId
            return True
    return False


def isColFull(board, column):
    return False if board[0][column] == 0 else True


def countNumPossibleFours(board, k):
    # returns the number of possible 4's that an id can make
    if (checkForWinner(board)) == k:
        return 1e10
    num = 0
    # vertical 4's
    for i in range(NUM_CELLS - 4 + 1):
        for j in range(NUM_CELLS):
            if ((board[i][j] == k or board[i][j] == 0) and (board[i + 1][j] == k or board[i + 1][j] == 0) and (
                    board[i + 2][j] == k or board[i + 2][j] == 0) and (board[i + 3][j] == k or board[i + 3][j] == 0)):
                num += 1
    # check all horizontal 4's
    for i in range(NUM_CELLS):
        for j in range(NUM_CELLS - 4 + 1):
            if ((board[i][j] == k or board[i][j] == 0) and (board[i][j + 1] == k or board[i][j + 1] == 0) and (
                    board[i][j + 2] == k or board[i][j + 2] == 0) and (board[i][j + 3] == k or board[i][j + 3] == 0)):
                num += 1

    # check all TRBL 4's
    for i in range(int(NUM_CELLS / 2) + 1):
        for j in range(int(NUM_CELLS / 2 - 1), NUM_CELLS):
            if ((board[i][j] == k or board[i][j] == 0) and (board[i + 1][j - 1] == k or board[i + 1][j - 1] == 0) and (
                    board[i + 2][j - 2] == k or board[i + 2][j - 2] == 0) and (
                    board[i + 3][j - 3] == k or board[i + 3][j - 3] == 0)):
                num += 1

    # check all TLBR 4s
    for i in range(0, int(NUM_CELLS / 2) + 1):
        for j in range(0, int(NUM_CELLS / 2) + 1):
            if ((board[i][j] == k or board[i][j] == 0) and (board[i + 1][j + 1] == k or board[i + 1][j + 1] == 0) and (
                    board[i + 2][j + 2] == k or board[i + 2][j + 2] == 0) and (
                    board[i + 3][j + 3] == k or board[i + 3][j + 3] == 0)):
                num += 1
    return num

def evaluateBoard(board):
    pass
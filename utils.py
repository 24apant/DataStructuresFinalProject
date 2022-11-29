import pygame

from settings import *


class Board:
    def __init__(self):
        self.contents = []
        for i in range(NUM_ROWS):
            self.contents.append([])
            for j in range(NUM_COLS):
                self.contents[i].append(0)

    def addCell(self, column, playerId):
        for i in range(NUM_ROWS - 1, -1, -1):
            if self.contents[i][column] == 0:
                self.contents[i][column] = playerId
                return True
        return False

    def checkForWinner(self):
        # check all vertical 4's
        board = self.contents
        possWinners = [1, -1]

        t = 0
        for i in range(NUM_COLS):
            if board[0][i] != 0:
                t+=1
        if t == NUM_COLS:
            return 2

        for i in range(NUM_ROWS - 4 + 1):
            for j in range(NUM_COLS):
                for k in possWinners:
                    if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == k:
                        return k
        # check all horizontal 4's
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS - 4 + 1):
                for k in possWinners:
                    if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == k:
                        return k
        # check all TRBL 4's
        for i in range(NUM_ROWS - 4 + 1):
            for j in range(NUM_COLS - 1, NUM_COLS - 4 - 1, -1):
                for k in possWinners:
                    if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3] == k:
                        print("diag")
                        return k
        # check all TLBR 4s
        for i in range(0, NUM_ROWS - 4 + 1):
            for j in range(0, NUM_COLS - 4 + 1):
                for k in possWinners:
                    if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == k:
                        print("diag 2")
                        return k
        return 0

    def isColFull(self, column):
        return False if self.contents[0][column] == 0 else True

    def evaluateBoard(self):
        if (self.checkForWinner()) == -1:  # AI
            return -1e10
        elif (self.checkForWinner()) == 1:
            return 1e10
        evalBoard = [
            [3, 4, 5, 7, 5, 4, 3],
            [4, 6, 8, 10, 8, 6, 4],
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [3, 4, 5, 7, 5, 4, 3]
        ]

        # taken from https://stackoverflow.com/questions/56721256/my-implementation-of-the-evaluation-function-and
        # -alpha-beta-pruning-for-connect
        num = 0
        for i in range(len(evalBoard)):
            for j in range(len(evalBoard[i])):
                if self.contents[i][j] == -1:
                    num -= evalBoard[i][j]
                elif self.contents[i][j] == 1:
                    num += evalBoard[i][j]
        return num

    def setBoard(self, newBoard):
        self.contents = newBoard

    def print(self):
        # prints the board in a nice way
        print()
        for i in range(len(self.contents)):
            print(self.contents[i])
        print("Score: " + str(self.evaluateBoard()))
        print()


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

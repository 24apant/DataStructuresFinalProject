from settings import *
import pygame


# relevant classes for Connect 4 game

# Board class - contains the board and relevant methods
class Board:
    def __init__(self):
        self.contents = []
        for i in range(NUM_ROWS):
            self.contents.append([])
            for j in range(NUM_COLS):
                self.contents[i].append(0)

    # Adds a cell with ID 'playerId' at a Column 'column' into the board, returns true if added
    def addCell(self, column, playerId):
        for i in range(NUM_ROWS - 1, -1, -1):
            if self.contents[i][column] == 0:
                self.contents[i][column] = playerId
                return True
        return False

    # Method checks if any player has won the game, returns 0 if not
    def checkForWinner(self):
        # check all vertical 4's
        board = self.contents
        possWinners = [1, -1]

        t = 0
        for i in range(NUM_COLS):
            if board[0][i] != 0:
                t += 1
        if t == NUM_COLS:
            return 2  # tie

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
                        return k
        # check all TLBR 4s
        for i in range(0, NUM_ROWS - 4 + 1):
            for j in range(0, NUM_COLS - 4 + 1):
                for k in possWinners:
                    if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == k:
                        return k
        return 0  # no win

    # Helper method, checks if column is full
    def isColFull(self, column):
        return False if self.contents[0][column] == 0 else True

    # Minimax "scoring function" - uses a table to show the AI where we want its pieces to be
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
        num = 0
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
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


# Level class - Class for different scenarios in Connect4Trainer
class Level:
    def __init__(self, x, y, scNum):
        self.x = x
        self.y = y
        self.width = LEVEL_WIDTH
        self.height = LEVEL_HEIGHT
        self.color = LEVEL_COLOR
        self.scNum = scNum
        self.xBounds = [self.x, self.x + self.width]
        self.yBounds = [self.y, self.y + self.width]

    def draw(self, gui, my_font, color):
        pygame.draw.rect(gui, color, [self.x, self.y, self.width, self.height])
        # blit text on screen
        txt = my_font.render('SCENARIO ' + str(self.scNum), False, (0, 0, 0))
        midX = self.x + (self.width // 7)
        midY = self.y + (self.height // 3)
        gui.blit(txt, (midX, midY))

    def isSelected(self, mX, mY):
        return self.xBounds[0] < mX < self.xBounds[1] and self.yBounds[0] < mY < self.yBounds[1]


# Node class for minimax
class Node:
    def __init__(self, board):
        self.children = []
        for _ in range(NUM_COLS):
            self.children.append(None)
        self.board = board  # this will be the key position
        self.score = 0
        self.isParent = False

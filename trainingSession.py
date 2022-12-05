import minimax
import oldBoards
import pygame
import classes
from utils import *


# create a new board with the oldBoard Level needed
class trainingSesh:
    def __init__(self, levelNum):
        self.board = classes.Board()
        self.board.setBoard(oldBoards.boards[levelNum - 1])
        self.answerMoves = oldBoards.boardSols[levelNum - 1]
        self.activeCol = -1
        self.col_dims = []
        self.game_over = False
        self.bg = BACKGROUND_COLOR
        self.currentPlayer = 1

        self.currentMove = 0
        self.ai = minimax.minimaxAlgorithm(self.board, depth=AI_DEPTH)

        # initialize col dims
        for i in range(NUM_COLS):
            self.col_dims.append([BUFFER_AROUND + (CELL_SIZE * i), BUFFER_AROUND + (i * CELL_SIZE) + CELL_SIZE])

        # get board associated to level num

    def draw(self, gui):
        drawBoard(self.board, gui, self.activeCol)

    def updateGameFromWinner(self):
        if self.board.checkForWinner() != 0:
            self.game_over = True
            if self.board.checkForWinner() == 1:
                self.bg = YELLOW_PLAYER_COLOR
                print("Winner")

            elif self.board.checkForWinner() == 2:
                self.bg = (255, 255, 255)
                print("Tie")

            else:
                self.bg = (255, 0, 0)
                print("Loser")

    def doClick(self, mX, mY, gui, event):
        for i in range(NUM_COLS):
            if self.col_dims[i][0] < mX < self.col_dims[i][1]:
                self.activeCol = i
                break

        if event.type == pygame.QUIT:
            self.game_over = True
        if event.type == pygame.MOUSEBUTTONUP and not self.game_over:
            # self.updateGameFromWinner()

            if self.answerMoves[self.currentMove] == self.activeCol and not self.game_over and self.board.addCell(
                    self.activeCol, self.currentPlayer):

                # This means that the move was correct
                print("Logger: Correct move at " + str(self.activeCol) + "!")
                self.currentMove += 1
                self.currentPlayer *= -1
                self.updateGameFromWinner()

                if not self.game_over and self.currentPlayer == -1:
                    self.ai.updateBoard(self.board)
                    if self.ai.getBestMoveFromTreeAB() is not None and self.board.isColFull(
                            self.ai.getBestMoveFromTreeAB()):
                        print("AI messed up")
                    if self.board.addCell(self.ai.getBestMoveFromTreeAB(), self.currentPlayer):
                        self.currentPlayer *= -1
                if self.currentMove >= len(self.answerMoves):
                    # Training is done
                    print("Congrats! You have completed this training!")
                    self.game_over = True
                    return "done"
                return "correct"

                self.draw(gui)
                pygame.display.update()
                # check if the move is the right move
            elif self.answerMoves[self.currentMove] != self.activeCol:
                return "incorrect"

            # check if player move was right, otherwise don't place
            # if right, then we play AI move

            if self.currentMove >= len(self.answerMoves):
                # Training is done
                print("Congrats! You have completed this training!")
                self.game_over = True
                return "correct"

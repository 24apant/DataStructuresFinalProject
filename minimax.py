# makes a tree that goes through the first n possible moves
# calculates the score
import copy
import math
import classes
from utils import *
import random


class minimaxAlgorithm:
    def __init__(self, board, depth=1, playerId=-1) -> None:
        self.depth = depth
        self.root = Node(board)
        self.root.score = self.__evaluateBoard(self.root)
        self.numBoards = 0
        self.numBoardsAB = 0
        self.alreadyFoundBoards = set()
        self.playerId = playerId
    def updateBoard(self, board):
        self.root.board = board
        self.alreadyFoundBoards = set()
        self.populateTree()
    def getBestMoveDebug(self):
        self.numBoards = 0
        ret = self.__getBestMoveRecAB(self.root, self.playerId, math.inf, -math.inf)[0]
        if ret is None:
            ret = random.randint(0, NUM_COLS - 1)
            while self.root.board.isColFull(ret):
                ret = random.randint(0, NUM_COLS - 1)
        return ret
    def getBestMoveFromTreeAB(self):
        self.numBoardsAB = 0
        ret =  self.__getBestMoveRecAB(self.root, self.playerId, math.inf, -math.inf)[0]
        if ret is None:
            ret = random.randint(0, NUM_COLS-1)
            while self.root.board.isColFull(ret):
                ret = random.randint(0, NUM_COLS-1)
        return ret
    def __getBestMoveRecAB(self, current, playerId, alpha, beta, print=False):
        if not current.isParent:
            return None, self.__evaluateBoard(current)

        if playerId == -1:
            # get all children and compare vals
            oldScore = math.inf
            bestMove = None
            for i in range(NUM_COLS):
                if isinstance(current.children[i], Node) and current.board.checkForWinner() == 0:
                    if print: current.children[i].board.print()

                    newMove, newScore = self.__getBestMoveRecAB(current.children[i], playerId * -1, alpha, beta)
                    self.numBoardsAB += 1

                    if newScore < oldScore and not self.root.board.isColFull(i):
                        bestMove = i
                        oldScore = newScore
                    if oldScore < alpha:
                        alpha = oldScore
                    if beta >= alpha:
                        break
            return (bestMove, oldScore)

        elif (playerId == 1):
            oldScore = -math.inf
            bestMove = None
            for i in range(NUM_COLS):
                if isinstance(current.children[i], Node) and current.board.checkForWinner() == 0:
                    if print: current.children[i].board.print()
                    self.numBoardsAB += 1
                    newMove, newScore = self.__getBestMoveRecAB(current.children[i], playerId * -1, alpha, beta)
                    if newScore > oldScore and not self.root.board.isColFull(i):
                        bestMove = i
                        oldScore = newScore
                    if oldScore > beta:
                        beta = oldScore
                    if beta >= alpha:
                        break
            return (bestMove, oldScore)


    def populateTree(self):
        self.__populateTreeRec(self.root, 0, self.playerId)

    def __populateTreeRec(self, current, depth, playerId):
        # try to do one layer
        pB = self.__genAllPossibleBoards(current, playerId)
        if (len(pB) == 0):
            return
        if depth >= self.depth:
            return
        if (DEBUG_PRINT_DEPTH_BOARDS):
            for b in pB:
                b.print()

        current.isParent = True
        for i in range(len(pB)):
            current.children[i] = (Node(pB[i]))
            current.children[i].score = self.__evaluateBoard(current.children[i])
            self.__populateTreeRec(current.children[i], depth + 1, playerId * -1)

    def __genAllPossibleBoards(self, node, playerId):
        allPossBoards = []
        # want to check 8 times
        for col in range(NUM_COLS):
            newBoard = classes.Board()
            newBoard.setBoard(copy.deepcopy(node.board.contents))
            if not (newBoard.isColFull(col) and not convBoardToB3(newBoard) in self.alreadyFoundBoards):
                self.alreadyFoundBoards.add(convBoardToB3(newBoard))
                newBoard.addCell(col, playerId)
                allPossBoards.append(newBoard)
        return allPossBoards

    def __evaluateBoard(self, node):
        return node.board.evaluateBoard()


class Node:
    def __init__(self, board):
        self.children = []
        for _ in range(NUM_COLS):
            self.children.append(None)
        self.board = board  # this will be the key position
        self.score = 0
        self.isParent = False


if __name__ == "__main__":
    board = classes.Board()
    # board is [
    # [0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0]
    # [0,0,0,1,0,0,0]
    # ]

    test = minimaxAlgorithm(board, 4)
    test.populateTree()
    print(test.getBestMoveFromTreeAB())
    print(test.numBoardsAB)
    test.root.board.print()

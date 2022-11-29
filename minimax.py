# makes a tree that goes through the first n possible moves
# calculates the score
import copy
import math

from utils import *


class minimaxAlgorithm:
    def __init__(self, board, depth=1) -> None:
        self.depth = depth
        self.root = Node(board)
        self.root.score = self.__evaluateBoard(self.root)

    def updateBoard(self, board):
        self.root.board = board
        self.populateTree()

    def getBestMoveFromTree(self):
        return self.__getBestMoveRec(self.root, -1)[0]

    def __getBestMoveRec(self, current, playerId):
        if not current.isParent:
            return (None, self.__evaluateBoard(current))

        if playerId == -1:
            # get all children and compare vals
            oldScore = math.inf
            bestMove = None
            for i in range(NUM_COLS):
                if isinstance(current.children[i], Node):
                    newMove, newScore = self.__getBestMoveRec(current.children[i], playerId * -1)
                    if newScore < oldScore and not self.root.board.isColFull(i):
                        bestMove = i
                        oldScore = newScore
            return (bestMove, oldScore)

        elif (playerId == 1):
            oldScore = -math.inf
            bestMove = None
            for i in range(NUM_COLS):
                if isinstance(current.children[i], Node):
                    newMove, newScore = self.__getBestMoveRec(current.children[i], playerId * -1)
                    if newScore > oldScore and not self.root.board.isColFull(i):
                        bestMove = i
                        oldScore = newScore
            return (bestMove, oldScore)

    def populateTree(self):
        self.__populateTreeRec(self.root, 0, -1)

    def __populateTreeRec(self, current, depth, playerId):
        # try to do one layer
        pB = self.__genAllPossibleBoards(current, playerId)
        if (len(pB) == 0):
            return
        if (depth >= self.depth):
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
            newBoard = Board()
            newBoard.setBoard(copy.deepcopy(node.board.contents))
            if not (newBoard.isColFull(col)):
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
    board = Board()
    test = [[0, 0, -1, -1, 0, 0, 0],
            [0, 0, 1, 1, 1, -1, 0],
            [0, 0, -1, -1, -1, 1, 0],
            [0, 0, 1, 1, 1, -1, 0],
            [0, 0, 1, 1, -1, -1, 0],
            [1, 1, -1, 1, -1, -1, 0]]
    board.setBoard(test)
    # board is [
    # [0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0]
    # [0,0,0,0,0,0,0,0]
    # ]

    test = minimaxAlgorithm(board, 3)
    test.populateTree()
    print(test.getBestMoveFromTree())

# makes a tree that goes through the first n possible moves
# calculates the score
from settings import *
from utils import *
import copy


class minimaxAlgorithm:
    def __init__(self, board, depth=1) -> None:
        self.depth = depth
        self.root = Node(board)
        self.root.score = self.__evaluateBoard(self.root)

    def updateBoard(self, board):
        self.root.board = board
        self.__populateTree()

    def getBestMoveFromTree(self):
        return self.__getBestMoveRec(self.root, 0)

    def __getBestMoveRec(self, current, depth):
        pass
    def populateTree(self):
        self.__populateTreeRec(self.root, 0, -1)
    def __populateTreeRec(self, current, depth, playerId):
        self.nlevels = 0
        # try to do one layer
        pB = self.__genAllPossibleBoards(current, playerId)
        if (len(pB) == 0):
            return
        if (depth > self.depth):
            return
        current.isParent = True
        self.nlevels += 1
        for i in range(len(pB)):
            current.children[i] = (Node(pB[i]))
            current.children[i].score = self.__evaluateBoard(current.children[i])
            self.__populateTreeRec(current.children[i], depth + 1, playerId * -1)

    def __genAllPossibleBoards(self, node, playerId):
        allPossBoards = []
        # want to check 8 times
        for col in range(NUM_CELLS):
            newBoard = copy.deepcopy(node.board)
            if (not (isColFull(newBoard, col))):
                insertCellIntoBoard(newBoard, col, playerId)
                allPossBoards.append(newBoard[:])
        return allPossBoards

    def __getBestAIChild(self, node):
        lowestScore = 1e10
        bestPosition = -1
        for i in range(len(node.children)):
            if (node.children[i] is not None and node.children[i].score < lowestScore):
                lowestScore = node.children[i].score
                bestPosition = i
        node.score = lowestScore
        return [lowestScore, bestPosition]

    def __getBestHumanChild(self, node):
        highestScore = -1e10
        bestPosition = -1
        for i in range(len(node.children)):
            if (node.children[i] is not None and node.children[i].score > highestScore):
                highestScore = node.children[i].score
                bestPosition = i
        node.score = highestScore
        return [highestScore, bestPosition]

    def __evaluateBoard(self, node):
        # eval function idea from: https://stackoverflow.com/questions/10985000/how-should-i-design-a-good-evaluation-function-for-connect-4
        # 1st response
        b = node.board
        # find number of possible 4's in rows that each player can make and find difference
        return (countNumPossibleFours(b, 1) - countNumPossibleFours(b, -1))


class Node:
    def __init__(self, board):
        self.children = []
        for _ in range(NUM_CELLS):
            self.children.append(None)
        self.board = board  # this will be the key position
        self.score = 0
        self.isParent = False


if __name__ == "__main__":
    board = []
    for i in range(NUM_CELLS):
        board.append([])
        for j in range(8):
            board[i].append(0)

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

    test = minimaxAlgorithm(board)
    test.populateTree()
    print(test.getBestMoveFromTree())

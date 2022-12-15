# This file contains necessary methods for AI and minimax function

import copy  # Used to deep copy arrays to prevent parent editing
import math  # Used for infinity, min, and max
from funcs.utils import *
import random  # This is possibly something I can fix, but the AI returns None if it knows the player has a forced win.
from funcs.classes import Node


class minimaxAlgorithm:
    def __init__(self, board, depth=1, playerId=-1):
        self.depth = depth  # The depth the AI will go to. Default is 4
        self.root = Node(board)  # Root node of the minimax, the current state of the game
        self.root.score = self.__evaluateBoard(self.root)  # evaluation of the current state
        self.numBoards = 0  # Debugging and runtime info for normal minimax
        self.numBoardsAB = 0  # Debugging and runtime info for minimax with AB pruning
        self.alreadyFoundBoards = set()  # Hashset where we store previous boards to prevent duplicate states
        self.playerId = playerId  # ID of the AI player

    # Sets a new board, updates the tree and resets the set
    def updateBoard(self, board):
        self.root.board = board
        self.alreadyFoundBoards = set()
        self.populateTree()

    # Gets the best move from a *populated* tree - must populate the tree first
    def getBestMoveFromTreeAB(self):
        self.numBoardsAB = 0
        ret = self.__getBestMoveRecAB(self.root, self.playerId, math.inf, -math.inf)[0]
        if ret is None:  # If the AI knows it's going to lose, return a random move
            ret = random.randint(0, NUM_COLS - 1)
            while self.root.board.isColFull(ret):
                ret = random.randint(0, NUM_COLS - 1)
        return ret

    # Prints the boards that the AI iterates through, also gets best move
    def getBestMoveDebug(self):
        self.numBoards = 0  # If the AI knows it's going to lose, return a random move
        ret = self.__getBestMoveRecAB(self.root, self.playerId, math.inf, -math.inf, print=True)[0]
        if ret is None:
            ret = random.randint(0, NUM_COLS - 1)
            while self.root.board.isColFull(ret):
                ret = random.randint(0, NUM_COLS - 1)
        return ret

    # Recursive method for getting best move - explained
    def __getBestMoveRecAB(self, current, playerId, alpha, beta, print=False):
        # Base case - if the board is at the max depth or the board is 'terminal'
        if not current.isParent:
            return None, self.__evaluateBoard(current)
            # returns no move (right now it doesn't matter), but more importantly the score of the state

        # recursive switch -- the method is dependent on whos 'turn' it is
        if playerId == -1:  # AI
            # get all children and compare vals
            oldScore = math.inf
            bestMove = None
            for i in range(NUM_COLS):
                if isinstance(current.children[i], Node) and current.board.checkForWinner() == 0:
                    if print: current.children[i].board.print()

                    # Goes through each child, makes sure that the child is not terminal and is a Node

                    newMove, newScore = self.__getBestMoveRecAB(current.children[i], playerId * -1, alpha, beta)
                    self.numBoardsAB += 1

                    # finds best move, uses alpha-beta technique to return boards that don't need to be checked
                    if newScore < oldScore and not self.root.board.isColFull(i):
                        bestMove = i
                        oldScore = newScore
                    if oldScore < alpha:
                        alpha = oldScore
                    if beta >= alpha:
                        break
            return bestMove, oldScore

        elif playerId == 1:  # Human
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
        # finds all boards for node
        pB = self.__genAllPossibleBoards(current, playerId)
        # base case: no more boards can be made
        if len(pB) == 0:
            return
        # or depth is reached
        if depth >= self.depth:
            return
        # debug printing boards that are made -- settings
        if DEBUG_PRINT_DEPTH_BOARDS:
            for b in pB:
                b.print()
        # makes node parent if base cases are passed
        current.isParent = True
        for i in range(len(pB)):
            # adds a new node for each possible board, recurse with child node
            current.children[i] = (Node(pB[i]))
            current.children[i].score = self.__evaluateBoard(current.children[i])
            self.__populateTreeRec(current.children[i], depth + 1, playerId * -1)

    # Finds all possible moves from a board with a certain player's turn
    def __genAllPossibleBoards(self, node, playerId):
        allPossBoards = []
        # want to check 1 time for each column
        for col in range(NUM_COLS):
            newBoard = classes.Board()
            newBoard.setBoard(
                copy.deepcopy(node.board.contents))  # we use deepcopy here to make sure we don't edit the current board
            if not (newBoard.isColFull(col) and not convBoardToB3(newBoard) in self.alreadyFoundBoards):
                self.alreadyFoundBoards.add(convBoardToB3(newBoard))
                newBoard.addCell(col, playerId)
                allPossBoards.append(newBoard)
        return allPossBoards

    def __evaluateBoard(self, node):
        return node.board.evaluateBoard()


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

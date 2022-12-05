# connect 4 pygame
import sys

import pygame

import minimax
import trainingSession
import utils
from utils import *
import keyboard
import classes
import oldBoards

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 15)
game_over = False
seshActive = False

levelSelected = -1
sesh = trainingSession.trainingSesh(1)
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
bubbleTxt = pygame.transform.scale(pygame.image.load("txtBubble.png").convert(), BUBBLE_TEXT_SIZE)
BubbleMessage = "Try out a move!"

clock = pygame.time.Clock()
bg = BACKGROUND_COLOR  # background is dynamic
levs = []

for i in range(3):
    levs.append([])
    for j in range(3):
        # add a level for each one
        levs[i].append(classes.Level(90 + 150 * j, 200 + 100 * i, 3 * i + (j + 1)))
board = classes.Board()
fullSessionOver = False

while not fullSessionOver:
    screen.fill(bg)
    # make a level selector choosing levels from 1 to 10
    # draw levels and add click listeners in their box
    if not seshActive:
        for st in levs:
            for lev in st:
                lev.draw(screen, my_font, lev.color)
    elif seshActive:
        pygame.draw.rect(screen, (0, 0, 255), [BUFFER_AROUND, BUFFER_AROUND, GAME_WIDTH - BUFFER_AROUND - BUFFER_AROUND,
                                               GAME_HEIGHT - BUFFER_AROUND - BUFFER_AROUND])
        sesh.draw(screen)
        screen.blit(bubbleTxt, BUBBLE_TEXT_TL_ANCHOR)
        blitBubbleContent(BubbleMessage, my_font, screen)
        blitBubbleContent("", my_font, screen, exit=True)
        if not sesh.game_over:
            blitBubbleContent("", my_font, screen, exit=False,
                              hint=oldBoards.boardHintMsgs[levelSelected - 1][sesh.currentMove])
            pass

    for event in pygame.event.get():
        mX, mY = pygame.mouse.get_pos()
        if not seshActive:
            for st in levs:
                for l1 in st:
                    if l1.isSelected(mX, mY):
                        l1.draw(screen, my_font, (255, 255, 255))
        else:
            ret = sesh.doClick(mX, mY, screen, event)
            if ret == "incorrect":
                # blit incorrect
                BubbleMessage = "Incorrect! Try a different move"
            elif ret == "correct":
                BubbleMessage = "Correct! Find the next move"
            elif ret == "done":
                BubbleMessage = oldBoards.boardCompleteMsgs[levelSelected - 1]
            if keyboard.is_pressed("Esc"):
                screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
                seshActive = False

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # go to training session
            if not seshActive:
                for st in levs:
                    for l1 in st:
                        if l1.isSelected(mX, mY):
                            # create a training sesh with
                            if l1.scNum >= len(oldBoards.boards):
                                print("Coming Soon!")
                            else:
                                levelSelected = l1.scNum
                                sesh = trainingSession.trainingSesh(l1.scNum)
                                seshActive = True
                                BubbleMessage = "Try out a move!"

                                # init sesh
                                screen = pygame.display.set_mode((TRAINER_WIDTH, GAME_HEIGHT))

    clock.tick(60)
    pygame.display.update()

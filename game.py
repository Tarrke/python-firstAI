#!./venv/bin/python

import pygame
from  pygame import draw
#from pygame.locals import *
from dots import dots
import time
from random import randint

white = pygame.Color("white")
black = pygame.Color("black")
green = pygame.Color("green")
lblue = pygame.Color(120,120,255, 0)


def areAllDotsDead(dots):
    for dot in dots:
        if not dot.dead :
            return False
    return True

# 2 - Initialize the game
pygame.init()

if not pygame.font.get_init():
    pygame.font.init()

font = pygame.font.Font(None, 24)


screenSize = (800, 600)
screen=pygame.display.set_mode(screenSize)

clock = pygame.time.Clock()

start = (400, 550)
goal = (400, 50)

dots.screenX = screenSize[0]
dots.screenY = screenSize[1]
dots.steps = 200
dots.vmax = 10
max_dots = 100



obstacle = []

gDot = dots(screenSize, "red", goal)
gDot.radius = 10

dots.setGoal((goal[0], goal[1], gDot.radius))

myDots = [ dots(screenSize, "black", start) for i in range(max_dots) ]

# Main Loop
while 1:
    # clear the screen before drawing it again
    screen.fill(white)
    # Draw informations
    text = font.render("Generation "+str(1), True, lblue)
    textRect = text.get_rect()
    textRect.topleft = (50, 20)
    screen.blit(text, textRect)
    # Draw dots
    pygame.draw.circle(screen, pygame.Color(gDot.color), gDot.getPos(), gDot.radius)
    for dot in myDots:
        pygame.draw.circle(screen, pygame.Color(dot.color), dot.getPos(), dot.radius)

    # Update the screen
    pygame.display.flip()

    # Loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            print("Quitting the game")
            pygame.quit()
            exit(0)

    # Update the elements
    for dot in myDots:
        dot.update()

    # End of Generation?
    if areAllDotsDead(myDots):
        for dot in myDots:
            print(dot.x, dot.y)
        break

    # Maintain at most 10 FPS
    clock.tick(10)

time.sleep(10)

print("All dots are dead")
pygame.quit()
#!./venv/bin/python

import pygame
#from pygame.locals import *
from dots import dots
import time
from random import randint

white = pygame.Color("white")
black = pygame.Color("black")
green = pygame.Color("green")


def areAllDotsDead(dots):
    for dot in dots:
        print(dot.dead)
        if not dot.dead :
            return False
    return True

# 2 - Initialize the game
pygame.init()
width, height = 800, 600
screenSize = (800, 600)
screen=pygame.display.set_mode(screenSize)

clock = pygame.time.Clock()

start = (400, 550)
goal = (400, 50)

myDots = [ dots(screenSize, "black", start) for i in range(1) ]

obstacle = []

gDot = dots(screenSize, "red", goal)
gDot.radius = 5



# 3 - Load images
#player = pygame.image.load("resources/images/dude.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(white)
    # Draw dots
    pygame.draw.circle(screen, pygame.Color(gDot.color), gDot.getPos(), gDot.radius)
    for dot in myDots:
        pygame.draw.circle(screen, pygame.Color(dot.color), dot.getPos(), dot.radius)
    # 6 - draw the screen elements
    #screen.blit(player, (100,100))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            print("Quitting the game")
            pygame.quit()
            exit(0)
    # 9 - update the elements
    for dot in myDots:
        dot.update()

    if areAllDotsDead(myDots):
        break

    #time.sleep(0.01)
    clock.tick(10)
    #print(dot1.dead)

print("All dots are dead")
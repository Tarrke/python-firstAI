#!./venv/bin/python

import pygame
#from pygame.locals import *
from dots import dots
import time
from random import randint

white = pygame.Color("white")
black = pygame.Color("black")
green = pygame.Color("green")

# 2 - Initialize the game
pygame.init()
width, height = 800, 600
screenSize = (800, 600)
screen=pygame.display.set_mode(screenSize)

myDots = [ dots(screenSize, "black", (randint(0,screenSize[0]), randint(0,screenSize[1]))) for i in range(100) ]

# 3 - Load images
#player = pygame.image.load("resources/images/dude.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(white)
    # Draw dots
    for dot in myDots:
        #print(dot.pos)
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

    time.sleep(0.01)
    #print(dot1.dead)
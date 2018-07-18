#!./venv/bin/python

import pygame
from pygame.locals import *
from dots import dots
import time

white = pygame.Color("white")
black = pygame.Color("black")
green = pygame.Color("green")

# 2 - Initialize the game
pygame.init()
width, height = 800, 600
screenSize = (800, 600)
screen=pygame.display.set_mode(screenSize)

myDots = []

dot1 = dots(screenSize)
dot2 = dots(screenSize)

myDots.append(dot1)
myDots.append(dot2)

dot1.x = 100
dot1.y = 100
dot1.velocity = (0, -1)

dot2.x = 200
dot2.y = 200
dot2.radius = 4
dot2.color = "green"
dot2.velocity = (0,1)

print(myDots[1].velocity)

# 3 - Load images
#player = pygame.image.load("resources/images/dude.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(white)
    # Draw dots
    for dot in myDots:
        pygame.draw.circle(screen, pygame.Color(dot.color), (dot.x, dot.y), dot.radius)
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
#!./venv/bin/python

import pygame
from  pygame import draw
from population import population
from dots import dots
import time
from random import randint

white = pygame.Color("white")
lblue = pygame.Color(120,120,255, 0)


#def areAllDotsDead(dotList):
#    for dot in dotList:
#        if not dot.dead :
#            return False
#    return True

#def countDead(dotList):
#    a = [ 1 for d in dotList if d.dead ]
#    return len(a)



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

#dots.screenX = screenSize[0]
#dots.screenY = screenSize[1]
#dots.steps = 200
#dots.vmax = 10
maxSteps = 50
max_dots = 200

obstacle = []

gDot = dots("red", goal)
gDot.radius = 10

myPop = population(max_dots, "black")

myPop.setGoal((goal[0], goal[1], gDot.radius))
myPop.setScreen(screenSize)
myPop.setStart(start)
myPop.setMaxStep(maxSteps)

myPop.generate()

while myPop.generation < 10:
    # Main Loop
    while 1:
        # clear the screen before drawing it again
        screen.fill(white)
        # Draw informations
        text = font.render("Generation "+str(myPop.generation), True, lblue)
        textRect = text.get_rect()
        textRect.topleft = (50, 20)
        screen.blit(text, textRect)
        text2 = font.render("Morts "+str(myPop.countDead()), True, lblue)
        textRect2 = text2.get_rect()
        textRect2.topleft = (50, 44)
        screen.blit(text2, textRect2)
        # Draw dots
        #pygame.draw.circle(screen, pygame.Color(gDot.color), gDot.getPos(), gDot.radius)
        gDot.render(screen)
        for dot in myPop.myDots:
            #pygame.draw.circle(screen, pygame.Color(dot.color), dot.getPos(), dot.radius)
            dot.render(screen)

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
        for dot in myPop.myDots:
            dot.update()
            # Kill session for our dots...
            # TODO

        # End of Generation?
        if myPop.areAllDotsDead():
            #for dot in myPop.myDots:
                #print(dot.x, dot.y, dot.evaluate())
            break

        # Maintain at most 10 FPS
        clock.tick(10)

    # Construct the waiting screen
    screen.fill(white)
    text = font.render("Generation "+str(myPop.generation), True, lblue)
    textRect = text.get_rect()
    textRect.topleft = (50, 20)
    screen.blit(text, textRect)
    text2 = font.render("Morts "+str(myPop.countDead()), True, lblue)
    textRect2 = text2.get_rect()
    textRect2.topleft = (50, 44)
    screen.blit(text2, textRect2)
    # Draw dots
    gDot.render(screen)
    for dot in myPop.myDots:
        dot.render(screen)

    myPop.naturalSelection()
    print("Getting generation", myPop.generation)
    #myPop.getBestDot()
    #myPop.markBestDot()

    fps = 10
    timeframe = 2
    frame = 0

    while frame < timeframe * fps:
        # Loop through the events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type==pygame.QUIT:
                # if it is quit the game
                print("Quitting the game")
                pygame.quit()
                exit(0)

        clock.tick(10)
        frame +=1


print("All dots are dead")
pygame.quit()
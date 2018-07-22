"""Dots are some points that runs on the screen from a start to a goal."""

from random import randint
from random import random
from math import pi

from pygame import Color
from pygame.math import Vector2
import pygame

class dots:
    """Class for our dots."""

    # Screen size
    screenX = 0
    screenY = 0

    # Goal position
    goalX = 0
    goalY = 0
    goalSize = 0

    steps = 200
    vmax = 10
    vmaxsquare = vmax * vmax

    @staticmethod
    def setGoal(goal):
        """Sets the goal
          - posX
          - posY
          - size
        """
        dots.goalX = goal[0]
        dots.goalY = goal[1]
        dots.goalSize = goal[2]

    def __init__(self, color, position):
        """Init comment"""
        self.x = position[0]
        self.y = position[1]
        self.color = Color(color)
        self.radius = 2
        self.velocity = [0,0]
        self.dead = False
        self.pos = (self.x, self.y)
        self.moves = []
        self.iter = 0
        self.deadTime = dots.steps
        self.hasReachedGoal = False
        self.colorString = color

        if len(self.moves) != dots.steps:
            self.init_moves()

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.getPos(), self.radius)

    def move(self):
        self.x, self.y = (self.x + self.velocity[0], self.y + self.velocity[1])

    def update(self):
        if( not self.dead ):
            self.brain()
            # Caution, brain can suicide dots
            if not self.dead:
                self.move()
                if self.x <= 2 or self.x >= dots.screenX-2 or self.y <= 2 or self.y >= dots.screenY-2:
                    self.x = max(0, min(self.x, dots.screenX))
                    self.y = max(0, min(self.y, dots.screenY))
                    self.killDot()
                d = (self.x - dots.goalX)*(self.x - dots.goalX) + (self.y - dots.goalY)*(self.y - dots.goalY)
                if d < self.goalSize*self.goalSize:
                    self.hasReachedGoal = True
                    self.killDot()

    def getPos(self):
        return (int(self.x), int(self.y))

    def killDot(self):
        self.deadTime = self.iter
        self.dead = True

    def brain(self):
        #print('Iter Beg:', self.iter)
        self.acc = (self.moves[self.iter].x, self.moves[self.iter].y)
        self.velocity = [self.velocity[0] + self.acc[0], self.velocity[1] + self.acc[1]]

        v_square = self.velocity[0]*self.velocity[0] + self.velocity[1]*self.velocity[1]

        if v_square > dots.vmaxsquare:
            self.velocity[0] = self.velocity[0] * (dots.vmaxsquare / v_square)**0.5
            self.velocity[1] = self.velocity[1] * (dots.vmaxsquare / v_square)**0.5

        v_square = self.velocity[0]*self.velocity[0] + self.velocity[1]*self.velocity[1]

        self.iter += 1
        if self.iter >= dots.steps:
            self.killDot()
        #print('Accel   :', self.acc)
        #print('velocity:', self.velocity, v_square)
        #print('Iter End:', self.iter)

        return True

    def init_moves(self):
        for _ in range(dots.steps):
            v = Vector2(0,0)
            r = random() * 360
            v.from_polar((1,r))
            self.moves.append(v)
        print(self.moves[0].x)

    def evaluate(self):
        """Returns an evaluation of dot:
            * has it reached the goal
            * how many steps did it take
        """
        d_goal = ((dots.goalX-self.x)*(dots.goalX-self.x)+(dots.goalY-self.y)*(dots.goalY-self.y))
        d_steps = self.deadTime * self.deadTime
        #print(self.colorString, self.hasReachedGoal, 100 + 10000/d_steps, '--', d_goal, 1/d_goal)
        if self.hasReachedGoal:
            return 100 + 10000/d_steps
        else:
            return 1/d_goal

    def setColor(self, colorString):
        self.color = Color(colorString)
        self.colorString = colorString

    def mutateBrain(self):
        mutationRate = 0.01 # Chance that a specific direction is mutated
        for acc in self.moves:
            r = random()
            if r < mutationRate:
                # Going an other way
                acc.from_polar((1, random()*360))

    def gimmeBabyBrain(self):
        return self.moves

    def setBrain(self, brain):
        self.moves = brain
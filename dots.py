from random import randint
from random import random
from math import pi

from pygame.math import Vector2

class dots:
    """Class for our dots."""
    def __init__(self, screen, color, position):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.radius = 2
        self.velocity = (0,0)
        self.dead = False
        self.screenX = screen[0]
        self.screenY = screen[1]
        self.pos = (self.x, self.y)
        self.moves = []
        self.m = [] # TODO: remove me
        self.init_moves()
        self.iter = 0
        self.steps = 100

    def move(self):
        self.x, self.y = (self.x + self.velocity[0], self.y + self.velocity[1])

    def update(self):
        if( not self.dead ):
            self.brain()
            self.move()
        if self.x <= 2 or self.x >= self.screenX-2 or self.y <= 2 or self.y >= self.screenY-2:
            self.dead = True

    def getPos(self):
        return (int(self.x), int(self.y))

    def brain(self):
        #if( self.x == self.moves[self.iter][0] and self.y == self.moves[self.iter][1]):
        #    self.iter += 1
        #print('Dot going from', self.x, self.y, 'to', self.moves[self.iter], self.iter)
        #dirX = (-self.x + self.moves[self.iter][0])
        #dirY = (-self.y + self.moves[self.iter][1])
        #if dirX != 0:
        #    dirX = int(dirX / abs(dirX))
        #if dirY != 0:
        #    dirY = int(dirY / abs(dirY))
        #
        self.acc = (self.moves[self.iter].x, self.moves[self.iter].y)
        self.velocity = (self.velocity[0] + self.acc[0], self.velocity[1] + self.acc[1])
        self.iter += 1
        if self.iter > self.steps:
            self.dead = True
        print('Accel   :', self.acc)
        print('velocity:', self.velocity)

        return True

    def init_moves(self):
        self.m = [ random() * 360 for i in range(100) ]
        print(self.m)
        for i in range(len(self.m)):
            v = Vector2(0,0)
            v.from_polar((1,self.m[i]))
            self.moves.append(v)
        #self.moves = [ Vector2(0,0) for i in range(len(self.m)) ]
        #self.moves = [ v.from_polar((1, self.m[i])) for i, v in enumerate(self.moves) ]
        print(self.moves[0].x)
        # self.moves = [ (randint(0,self.screenX), randint(0,self.screenY)) for i in range(self.steps)]
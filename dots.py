from random import randint
from random import random
from math import pi

from pygame.math import Vector2

class dots:
    """Class for our dots."""

    screenX = 0
    screenY = 0

    goalX = 0
    goalY = 0

    def __init__(self, screen, color, position):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.radius = 2
        self.velocity = [0,0]
        self.dead = False
        #self.screenX = screen[0]
        #self.screenY = screen[1]
        self.pos = (self.x, self.y)
        self.moves = []
        self.m = [] # TODO: remove me
        self.iter = 0
        self.steps = 200
        self.vmax = 10

        self.init_moves()
        self.vmaxsquare = self.vmax * self.vmax
        print(self.steps)

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
                    self.dead = True            
                d = (self.x - dots.goalX)*(self.x - dots.goalX) + (self.y - dots.goalY)*(self.y - dots.goalY)
                if d < 50:
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
        print('Iter Beg:', self.iter)
        self.acc = (self.moves[self.iter].x, self.moves[self.iter].y)
        self.velocity = [self.velocity[0] + self.acc[0], self.velocity[1] + self.acc[1]]

        v_square = self.velocity[0]*self.velocity[0] + self.velocity[1]*self.velocity[1] 

        if v_square > self.vmaxsquare:
            self.velocity[0] = self.velocity[0] * (self.vmaxsquare / v_square)**0.5
            self.velocity[1] = self.velocity[1] * (self.vmaxsquare / v_square)**0.5

        v_square = self.velocity[0]*self.velocity[0] + self.velocity[1]*self.velocity[1] 

        self.iter += 1
        if self.iter >= self.steps:
            self.dead = True
        print('Accel   :', self.acc)
        print('velocity:', self.velocity, v_square)
        print('Iter End:', self.iter)

        return True

    def init_moves(self):
        for i in range(self.steps):
            v = Vector2(0,0)
            r = random() * 360
            v.from_polar((1,r))
            self.moves.append(v)
        #self.moves = [ Vector2(0,0) for i in range(len(self.m)) ]
        #self.moves = [ v.from_polar((1, self.m[i])) for i, v in enumerate(self.moves) ]
        print(self.moves[0].x)
        # self.moves = [ (randint(0,self.screenX), randint(0,self.screenY)) for i in range(self.steps)]
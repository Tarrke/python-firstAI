from random import randint

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
        self.init_moves()
        self.iter = 0

    def move(self):
        self.x, self.y = (self.x + self.velocity[0], self.y + self.velocity[1])

    def update(self):
        if( not self.dead ):
            self.brain()
            self.move()
        if self.x <= 2 or self.x >= self.screenX-2 or self.y <= 2 or self.y >= self.screenY-2:
            self.dead = True

    def getPos(self):
        return (self.x, self.y)

    def brain(self):
        if( self.x == self.moves[self.iter][0] and self.y == self.moves[self.iter][1]):
            self.iter += 1
        print('Dot going from', self.x, self.y, 'to', self.moves[self.iter], self.iter)
        dirX = (-self.x + self.moves[self.iter][0])
        dirY = (-self.y + self.moves[self.iter][1])
        if dirX != 0:
            dirX = int(dirX / abs(dirX))
        if dirY != 0:
            dirY = int(dirY / abs(dirY))

        self.velocity = (dirX, dirY)
        print('velocity:', self.velocity)

        return True

    def init_moves(self):
        self.moves = [ (randint(0,self.screenX), randint(0,self.screenY)) for i in range(100)]
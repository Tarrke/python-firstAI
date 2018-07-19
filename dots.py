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

    def move(self):
        self.x, self.y = (self.x + self.velocity[0], self.y + self.velocity[1])

    def update(self):
        if( not self.dead ):
            self.move()
        if self.x <= 0 or self.x >= self.screenX or self.y <= 0 or self.y >= self.screenY:
            self.dead = True

    def getPos(self):
        return (self.x, self.y)
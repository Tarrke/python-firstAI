class dots:
    """Class for our dots."""
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.color = "black"
        self.radius = 2
        self.velocity = (0,0)
        self.dead = False
        self.screenX = screen[0]
        self.screenY = screen[1]

    def move(self):
        self.x, self.y = (self.x + self.velocity[0], self.y + self.velocity[1])

    def update(self):
        if( not self.dead ):
            self.move()
        if self.x <= 0 or self.x >= self.screenX or self.y <= 0 or self.y >= self.screenY:
            self.dead = True
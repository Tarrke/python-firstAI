"""A Population is a set of dots that form a generation."""

from dots import dots

class population:
    """Population population, oh my population"""

    def __init__(self, dotNumber=0, color="black"):
        self.myDots = []
        self.dotNumber = dotNumber
        self.Best = None
        self.start = (0,0)
        self.goal = (0,0,0)
        self.color = color
        self.bestDot = None


    def areAllDotsDead(self):
        for dot in self.myDots:
            if not dot.dead :
                return False
        return True

    def countDead(self):
        a = [ 1 for d in self.myDots if d.dead ]
        return len(a)

    def setGoal(self, goal):
        """Sets the goal for all dots on the population"""
        self.goal = goal
        dots.setGoal(goal)

    def setScreen(self, screenSize):
        dots.screenX = screenSize[0]
        dots.screenY = screenSize[1]

    def setStart(self, startPoint):
        self.start = startPoint

    def generate(self):
        self.myDots = [ dots(self.color, self.start) for i in range(self.dotNumber) ]

    def getBestDot(self):
        score = 0
        best = None
        #print("current best score:", score)
        for dot in self.myDots:
            s = dot.evaluate()
            #print("Checking ", s)
            if s > score:
                score = s
                best = dot
            #print("current best score:", score)
        self.bestDot = best
        return best

    def markBestDot(self):
        self.bestDot.setColor("green")
        self.bestDot.radius = 4

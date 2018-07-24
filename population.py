"""A Population is a set of dots that form a generation."""

from dots import dots
from random import random

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
        self.generation = 1
        self.maxSteps = 0

    def setMaxStep(self, steps):
        self.maxSteps = steps
        dots.steps = steps

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

    def calculateScoreSum(self):
        score = 0
        for dot in self.myDots:
            score += dot.evaluate()
        return score

    def selectParent(self):
        """Select a parent based on its perfromances at random.
        We get all scores on a line, then sum them. Then random on this line. Ence better performance leads to better chances to reproduce."""
        scoreSum = self.calculateScoreSum()
        r = random() * scoreSum

        runningScoreSum = 0
        i = 0
        for dot in self.myDots:
            runningScoreSum += dot.evaluate()
            if runningScoreSum > r:
                print("~~choose dot", i)
                return dot
            i += 1

    def naturalSelection(self):
        newDots = [ dots(self.color, self.start) for i in range(self.dotNumber) ]
        self.getBestDot()

        newDots[0] = self.bestDot
        self.markBestDot()
        newDots[0].x = self.start[0]
        newDots[0].y = self.start[1]
        newDots[0].dead = False
        newDots[0].iter = 0

        for dot in newDots[1:]:
            dot.setBrain(self.selectParent().gimmeBabyBrain())
            dot.mutateBrain()

        for dot in newDots:
            print(hex(id(dot.moves)))

        self.myDots = newDots
        print("Natural Selection is done.")
        #for dot in self.myDots:
        #    print(dot.dead)
        self.generation += 1

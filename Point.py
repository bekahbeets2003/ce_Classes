class Point():

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** .5

    def move(self, dx, dy):
        

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

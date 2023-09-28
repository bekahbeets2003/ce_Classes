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
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)


import test

point = Point(1, 2)
test.testEqual(point.x, 1)
test.testEqual(point.y, 2)

# native assert statement, assignments to debug are illegal,
# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assert_stmt
point2 = Point(3, 4)
assert (point2.x == 3)
assert (point2.y == 4, 'custom error message')

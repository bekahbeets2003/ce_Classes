class Point():

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # the hypotenuse assuming right triangle
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

point.move(5,8)
# round hypotenuse to the nearest whole number
hypotenuse = round(point.distanceFromOrigin(), 0)
print(hypotenuse)
# does an implicit match of 12.0 to 12
test.testEqual(hypotenuse, 12)

# native assert statement, assignments to debug are illegal,
# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assert_stmt
point2 = Point(3, 4)
assert (point2.x == 3)
assert (point2.y == 4, 'custom error message')

point2.move(10,3)
# round hypotenuse to the nearest whole number
hypotenuse2 = round(point2.distanceFromOrigin(), 0)
# does an implicit match of 15.0 to 15
assert(hypotenuse2, 15)
print(hypotenuse2)

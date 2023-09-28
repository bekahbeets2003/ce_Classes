class AppleBasket():

    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def __str__(self):
        return 'A basket of {} {} apples.'.format(self.apple_quantity, self.apple_color)

    def increase(self):
        self.apple_quantity = self.apple_quantity + 1

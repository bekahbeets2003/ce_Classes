# This is a sample Python script.
from Point import Point
from Bike import Bike
from BankAccount import BankAccount
from City import City


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import Point as Point


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    point = Point(1, 2)
    point2 = Point(3, 4)

    # point.x = 5
    # point2.x = 10

    print(point.getX())
    print(point2.getX())

    print(point.getY())
    print(point2.getY())

    print(point)
    print(point2)

    testOne = Bike('blue', 89.99)
    testTwo = Bike('purple', 25.0)

    t1 = BankAccount('Bob', 100)

    # map tuples to class
    city_names = ('San Antonio', 'San Diego', 'Oklahoma City', 'Detroit', 'NYC')
    city_states = ('TX', 'SD', 'OK', 'MI', 'NY')
    city_pop = (12345, 67890, 23456, 34567, 45678)

    cities = []
    city_tuples = zip(city_names, city_states, city_pop)
    for city_tup in city_tuples:
        name, state, pop = city_tup
        city = City(name, state, pop)  # instance of City class
        cities.append(city)
        print(city)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

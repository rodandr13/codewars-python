"""
You need to find, if given a multi-line string road, whether the speeding
car will crash or not.

A road will always contain the following:

The speeding car, O='`o, who's driver is too scared to turn.
The other cars, signified by X's. They will always be heading in the same
direction as the car.
The function returns true/ True if there are X's ahead of the speeding car
in the same lane, but returns false/False if the speeding car has already
passed all of the car's in the lane, or if its lane is empty.
"""

"""
def car_crash(road):
    return "O='`oX" in road.replace(' ', '')
"""


def car_crash(road):
    roads = road.split('\n')
    car = 'O=\'`o'
    other_cars = 'X'
    for line in roads:
        if car in line:
            return other_cars in line[line.index(car)::]

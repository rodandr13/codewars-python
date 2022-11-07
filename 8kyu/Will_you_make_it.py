"""
You were camping with your friends far away from home, but when it's time to go back,
you realize that your fuel is running out and the nearest pump is 50 miles away!
You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
"""


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


assert zero_fuel(50, 25, 2) == True
assert zero_fuel(100, 50, 1) == False

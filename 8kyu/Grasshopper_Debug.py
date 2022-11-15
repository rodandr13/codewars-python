"""
Your friend is traveling abroad to the United States so he wrote a program
to convert fahrenheit to celsius. Unfortunately his code has some bugs.

Find the errors in the code to get the celsius converter working properly.
"""


def convert_to_celsius(temperature):
  celsius = (temperature - 32) * (5/9)
  return celsius


def weather_info(temp):
    temperature = convert_to_celsius(temp)
    if (temperature > 0):
        return (str(temperature) + " is above freezing temperature")
    else:
        return (str(temperature) + " is freezing temperature")


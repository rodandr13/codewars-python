"""
Time to test your basic knowledge in functions! Return the odds from a list:

[1, 2, 3, 4, 5]  -->  [1, 3, 5]
[2, 4, 6]        -->  []
"""
"""
def odds(values):
        return [i for i in values if i%2]
"""


odds = lambda x: [a for a in x if a % 2 != 0]

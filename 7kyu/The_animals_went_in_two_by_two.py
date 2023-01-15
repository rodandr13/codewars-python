"""
A great flood has hit the land, and just as in Biblical times we need to get
the animals to the ark in pairs. We are only interested in getting one pair
of each animal, and not interested in any animals where there are less than
2....they need to mate to repopulate the planet after all!

You will be given a list of animals, which you need to check to see which
animals there are at least two of, and then return a dictionary containing
the name of the animal along with the fact that there are 2 of them to bring
onto the ark.

two_by_two(['goat', 'goat', 'rabbit', 'rabbit', 'rabbit', 'duck', 'horse', 'horse', 'swan'])
{'goat': 2, 'horse': 2, 'rabbit': 2}
"""
"""
def two_by_two(animals):
    return {x:2 for x in animals if animals.count(x) > 1} if animals else False
"""


def two_by_two(animals):
    if not animals:
        return False
    return {x: 2 for x in animals if animals.count(x) >= 2}

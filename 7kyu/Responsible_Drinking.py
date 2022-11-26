"""
Codewars Bar recommends you drink 1 glass of water per standard drink
so you're not hungover tomorrow morning.

Your fellow coders have bought you several drinks tonight in the form of
a string. Return a string suggesting how many glasses of water you should
drink to not be hungover.
"""


def hydrate(drink_string):
    drinks = drink_string.strip(",")
    count_drinks = [int(x) for x in drinks.split() if x.isdigit()]
    count_drinks = sum(count_drinks) if len(count_drinks) > 1 else count_drinks[0]
    glass = "glasses" if count_drinks > 1 else "glass"
    return f"{str(count_drinks)} {glass} of water"


assert hydrate("1 beer") == "1 glass of water"
assert hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer") == "10 glasses of water"
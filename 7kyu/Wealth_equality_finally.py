"""
The year is 2088 and the Radical Marxist Socialist People's Party (RMSPP) has
just seized power in Brazil.

Their first act in power is absolute wealth equality through coercive
redistribution.

Create a function that redistributes all wealth equally among all citizens.

Wealth is represented as an array/list where every index is the wealth of a
single citizen.
The function should mutate the input such that every index has the same amount
of wealth.
"""
"""
def redistribute_wealth(wealth):
    wealth[:] = [sum(wealth) / len(wealth)] * len(wealth)
"""


def redistribute_wealth(wealth):
    # mutate wealth
    sum1 = sum(wealth)
    average = sum1 / len(wealth)
    for i in range(len(wealth)):
        wealth[i] = average

"""
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years
"""


def nb_year(p0, percent, aug, p):
    count = 0
    while p > p0:
        count += 1
        p0 += int(p0 * (percent / 100) + aug)
    return count


assert nb_year(1500, 5, 100, 5000) == 15

def nb_year(p0, percent, aug, p):
    count = 0
    while p > p0:
        count += 1
        p0 += int(p0 * (percent / 100) + aug)

    print(p0)
    return count


assert nb_year(1500, 5, 100, 5000) == 15
assert nb_year(1500000, 2.5, 10000 == 2000000)
assert nb_year(1500000, 0.25, 1000 == 2000000)
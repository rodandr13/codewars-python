"""
https://www.codewars.com/kata/55ffb44050558fdb200000a4
"""


def sumDig_nthTerm(initVal, patternL, nthTerm):
    for i in range(nthTerm - 1):
        initVal += patternL[i%len(patternL)]
    return sum(map(int, list(str(initVal))))


assert sumDig_nthTerm(10, [2, 1, 3], 6) == 10
assert sumDig_nthTerm(10, [2, 1, 3], 15) == 10
assert sumDig_nthTerm(10, [2, 1, 3], 50) == 9

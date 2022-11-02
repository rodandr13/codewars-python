"""
In this Kata, you will be given a string and two indexes (a and b).
Your task is to reverse the portion of that string between those two indices inclusive.
"""


def solve(st,a,b):
    return st[:a] + st[a:b+1:][::-1] + st[b+1:]


assert solve("codewars",1,5) == "cawedors"
assert solve("codingIsFun",2,100) == "conuFsIgnid"
assert solve("FunctionalProgramming", 2,15) == "FuargorPlanoitcnmming"
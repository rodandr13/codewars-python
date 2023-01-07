"""
There are some stones on Bob's table in a row, and each of them can be red,
green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table
so that the stones in each pair of adjacent stones have different colours.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9
"""
"""
def solution(s):
    return sum(1 for i in range(len(s)) if i and s[i-1]==s[i])
"""


def solution(stones):
    count = 0
    for i in range(1, len(stones)):
        if stones[i-1] == stones[i]:
            count += 1
    return count

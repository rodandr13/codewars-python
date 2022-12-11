"""
You are a security guard at a large company, your job is to look over the
cameras. Finding yourself bored you decide to make a game from the people
walking in a hallway on one of the cameras. As many people walk past the
hallway you decide to figure out the minimum steps it will take before
2 people cross or come into contact with each other (assuming every person
takes a step at the same time).
"""
"""
import re

def contact(hallway):
    pairs = re.findall('>-*<', hallway)
    return min(map(len, pairs)) // 2 if pairs else -1
"""


import math


def contact(hallway):
    distance = []

    while(True):
        start = hallway.find(">")
        end = hallway.find("<", start)
        if start == -1 or end == -1:
            break
        distance.append(math.ceil((end - start) / 2))
        hallway = hallway[start + 1:]

    if not distance or len(distance) <= 1 and min(distance) < 0:
        return -1
    min_len = min([x for x in distance if x > 0])
    return min_len

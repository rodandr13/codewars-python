"""
https://www.codewars.com/kata/580559b17ab3396c58000abb
"""


def get_los_angeles_points(results):
    target = "Los Angeles"
    scores = 0
    for name, score in results:
        if name.startswith(target) and len(name.split()) == 3:
            last_word = name.split()[-1]
            if last_word.isalpha() and last_word[:1].isupper() and last_word[1:].islower():
                scored = score.split(":")[0]
                scores += int(scored)
    return scores

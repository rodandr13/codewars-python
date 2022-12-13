"""
You are working at a lower league football stadium and you've been tasked
with automating the scoreboard.

The referee will shout out the score, you have already set up the voice
recognition module which turns the ref's voice into a string, but the spoken
score needs to be converted into a pair for the scoreboard!

e.g. "The score is four nil" should return [4,0]
"""


def scoreboard(string):
    scores = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
              'seven': 7, 'eight': 8, 'nine': 9, 'nil': 0}
    result = [scores[x] for x in string.split() if x in scores]
    return result

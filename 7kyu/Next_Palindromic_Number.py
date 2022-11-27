"""
There were and still are many problem in CW about palindrome numbers and
palindrome strings. We suposse that you know which kind of numbers they are.
If not, you may search about them using your favourite search engine.

In this kata you will be given a positive integer, val and you have to create
the function next_pal()(nextPal Javascript) that will output the smallest
palindrome number higher than val.
"""


def next_pal(val):
    while (True):
        val += 1
        if str(val) == str(val)[::-1]:
            return val


assert next_pal(11), 22
assert next_pal(188), 191
assert next_pal(191), 202

"""
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good'
and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!',
if there are more than 2 return 'I smell a series!'. If there are no good
ideas, as is often the case, return 'Fail!'.
"""
"""
def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'
"""


def well(x):
    count_good = x.count("good")
    if not count_good:
        return "Fail!"
    return "Publish!" if count_good <= 2 else "I smell a series!"

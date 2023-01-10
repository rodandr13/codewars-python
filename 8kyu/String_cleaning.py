"""
Examples (input -> output)
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'
Your harried co-workers are looking to you for a solution to take this garbled
text and remove all of the numbers. Your program will take in a string and
clean out all numeric characters, and return a string with spacing and special
characters ~#$%^&!@*():;"'.,? all intact.
"""
"""
def string_clean(s):
    for d in '0123456789':
        s = s.replace(d, '')
    return s
"""


def string_clean(s):
    return "".join([x for x in s if not x.isdigit()])

"""
For this problem you must create a program that says who ate the last cookie.
If the input is a string then "Zach" ate the cookie. If the input is a float
or an int then "Monica" ate the cookie. If the input is anything else "the dog"
ate the cookie. The way to return the statement is: "Who ate the last cookie?
It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The
reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and
punctuation.

Please leave feedback for this kata. Cheers!
"""
"""
def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who
"""


def cookie(x):
    if not isinstance(x, bool) and isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    elif not isinstance(x, bool) and (isinstance(x, int) or isinstance(x, float)):
        return "Who ate the last cookie? It was Monica!"
    return "Who ate the last cookie? It was the dog!"

"""
You like building blocks. You especially like building blocks that are squares.
And what you even like more, is to arrange them into a square of square
building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up
with an ordinary rectangle! Those blasted things! If you just had a way
to know, whether you're currently working in vain… Wait! That's it!
You just have to check if your number of building blocks is a perfect square.

isSquare (-1) // => false
isSquare   3  // => false
isSquare   4  // => true
isSquare  25  // => true
isSquare  26  // => false
"""
"""
def is_square(n):
    return n >= 0 and (n**0.5) % 1 == 0
"""


def is_square(n):
    print(n)
    result = ((n ** 0.5) ** 2)
    return True if isinstance(result, float) and result == n else False

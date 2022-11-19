"""
Here you have to do some mathematical operations on a "dirty string".
This kata checks some basics, it's not too difficult.

So what to do?

Input: String which consists of two positive numbers (doubles) and exactly
one operator like +, -, * or / always between these numbers. The string is
dirty, which means that there are different characters inside too, not only
numbers and the operator. You have to combine all digits left and right,
perhaps with "." inside (doubles), and to calculate the result which has to be
rounded to an integer and converted to a string at the end.

Easy example:
Input: "gdfgdf234dg54gf*23oP42"
Output: "54929268" (because 23454*2342=54929268)
First there are some static tests, later on random tests too...
"""
"""
import re

def calculate_string(st): 
    st = re.sub(r'[^-+*/\d.]', '', st)
    result = eval(st)
    return str(int(round(result)))
"""


def calculate_string(st):
    expression = ""
    signs = "+-*/."
    result = {
        "+": lambda x, y: str(round(x + y)),
        "/": lambda x, y: str(round(x / y)),
        "*": lambda x, y: str(round(x * y)),
        "-": lambda x, y: str(round(x - y)),
    }
    for char in st:
        if char.isdigit() or char in signs:
            expression += char
    for char in signs:
        if char in expression:
            x, y = expression.split(char)
            return result[char](float(x), float(y))


assert calculate_string(";$%§fsdfsd235??df/sdfgf5gh.000kk0000") == "47"
assert calculate_string("sdfsd23454sdf*2342") == "54929268"
assert calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442") == "-210908"
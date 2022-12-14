"""
Write a function that removes every lone 9 that is inbetween 7s.

"79712312" --> "7712312"
"79797"    --> "777"
"""


def seven_ate9(str_):
    while str_.find("797") != -1:
        str_ = str_.replace("797", "77")
    return str_

"""
Write a function reverse which reverses a list
(or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)
"""


def reverse(lst):
    empty_list = list()            # use this!
    for i in range(len(lst)-1,-1,-1):
        empty_list.append(lst[i])
    return empty_list

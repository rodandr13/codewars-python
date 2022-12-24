"""
In this kata you are given a string for example:

"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"
"""


def remove_parentheses(s):
    bracket_count = 0
    result = ""
    for char in s:
        if char == "(":
            bracket_count += 1
        elif char == ")":
            bracket_count -= 1
        else:
            if bracket_count == 0:
                result += char
    return result

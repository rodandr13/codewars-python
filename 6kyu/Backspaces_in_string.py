"""
Assume "#" is like a backspace in string. This means that string "a#bc#d"
actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""
"""
def clean_string(s):
    result = []
    for char in s:
        if char == "#" and result:
            result.pop()
        elif char != "#":
            result.append(char)
    return "".join(result)
"""


def clean_string(s):
    result = ""
    for char in s:
        if char == "#":
            result = result[:-1]
        else:
            result += char
    return result

"""
Given a string, return true if the first instance of "x" in the string is
immediately followed by the string "xx".

tripleX("abraxxxas") → true
tripleX("xoxotrololololololoxxx") → false
tripleX("softX kitty, warm kitty, xxxxx") → true
tripleX("softx kitty, warm kitty, xxxxx") → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false
"""
""""
def triple_x(s: str) -> bool:
    return 0 <= s.find("x") == s.find("xxx") 

"""


def triple_x(s):
    index = s.find("x")
    if index != -1:
        return s[index+1:index+3] == "xx"
    return False

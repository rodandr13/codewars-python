"""
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or
camelCase in Java) for strings. All words must have their first letter
capitalized without spaces.

For instance:
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""

"""
def camel_case(string):
    return "".join(map(str.title, string.split()))
"""


def camel_case(string):
    return string.title().replace(" ", "")


assert camel_case("test case") == "TestCase"
assert camel_case("camel case method") == "CamelCaseMethod"
assert camel_case("say hello ") == "SayHello"

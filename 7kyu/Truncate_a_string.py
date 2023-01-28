"""
Truncate the given string (first argument) if it is longer than the given
maximum length (second argument). Return the truncated string with
a "..." ending.

Note that inserting the three dots to the end will add to the string length.

However, if the given maximum string length num is less than or equal to 3,
then the addition of the three dots does not add to the string length in
determining the truncated string.

Examples
('codewars', 9)  ==>  'codewars'
('codewars', 7)  ==>  'code...'
('codewars', 2)  ==>  'co...'
"""
"""
def truncate_string(s,n):
    return s if len(s)<=n else s[:n if n<=3 else n-3]+'...'
"""


def truncate_string(s, n):
    len_str = len(s)
    if len_str <= n:
        return s
    if n <= 3:
        return s[:n] + "..."
    result = s[:n-3] if len_str - n > 0 else s[:n]
    return result + "..."

"""
Given a positive integer n: 0 < n < 1e6, remove the last digit until you're
left with a number that is a multiple of three.

Return n if the input is already a multiple of three, and if no such number
xists, return null, a similar empty value, or -1.

Examples
1      => null
25     => null
36     => 36
1244   => 12
952406 => 9
"""


def prev_mult_of_three(n):
    if n % 3 == 0:
        return n
    num_str = str(n)
    for _ in num_str:
        num = int(num_str)
        if num % 3 == 0:
            return num
        num_str = num_str[:-1]
    return None


"""
The Collatz Conjecture states that for any positive natural number n,
this process:

if n is even, divide it by 2
if n is odd, multiply it by 3 and add 1
repeat
will eventually reach n = 1.

For example, if n = 20, the resulting sequence will be:

[ 20, 10, 5, 16, 8, 4, 2, 1 ]
Write a program that will output the length of the Collatz Conjecture
for any given n.
In the example above, the output would be 8.
"""
"""
def collatz(n):
    return 1 if n == 1 else 1 + collatz(3 * n + 1 if n % 2 else n // 2)
"""


def collatz(n):
    count = 1
    while n != 1:
        count += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return count

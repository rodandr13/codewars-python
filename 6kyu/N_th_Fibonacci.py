"""
I love Fibonacci numbers in general, but I must admit
I love some more than others.

I would like for you to write me a function that when given a number (n)
returns the n-th number in the Fibonacci Sequence.

For example:
   nth_fib(4) == 2
"""
"""
def nth_fib(n):
  a, b = 0, 1
  for i in range(n-1):
    a, b = b, a + b
  return a
"""


def nth_fib(n):
    if n < 0:
        return -1
    result = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        result[i] = result[i-1] + result[i-2]
    return result[n-1]


assert nth_fib(1) == 0
assert nth_fib(2) == 1
assert nth_fib(4) == 2
"""
Your goal is to return multiplication table for number that is always an
integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:
"""


def multi_table(number):
    result = ''
    for i in range(1, 11):
        result += str(i) + ' * ' + str(number) + ' = ' + str(i * number) + '\n'
    return result.rstrip('\n')

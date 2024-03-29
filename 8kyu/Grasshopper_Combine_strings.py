"""
Combine strings function
Create a function named (combine_names) that accepts two parameters
(first and last name). The function should return the full name.

Example:

combine_names('James', 'Stevens')
returns:

'James Stevens'
"""
"""
def combine_names(*args):
    return ' '.join(args)
"""


def combine_names(name, surname):
    return f"{name} {surname}"

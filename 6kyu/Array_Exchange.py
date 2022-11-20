""""
Array Exchange and Reversing

It's time for some array exchange! The objective is simple: exchange the
elements of two arrays in-place in a way that their new content is also reversed.

# before
my_list = ['a', 'b', 'c']
other_list = [1, 2, 3]

exchange_with(my_list, other_list)

# after
my_list == [3, 2, 1]
other_list == ['c', 'b', 'a']
"""
"""
def exchange_with(a, b):
    a[:], b[:] = b[::-1], a[::-1]
"""


def exchange_with(a, b):
    temp_a = [x for x in a[::-1]]
    temp_b = [x for x in b[::-1]]
    for i in range(len(temp_b)):
        a.append(temp_b[i])
    for i in range(len(temp_a)):
        b.append(temp_a[i])
    del a[:len(temp_a)]
    del b[:len(temp_b)]


a = ["1", "2", "3", "4", "5", "6", "7"]
b = ["a", "b", "c"]
exchange_with(a, b)
assert a == ["c", "b", "a"]
assert b == ["7", "6", "5", "4", "3", "2", "1"]


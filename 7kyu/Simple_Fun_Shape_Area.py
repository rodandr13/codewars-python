"""
Below we will define what and n-interesting polygon is and your task is to find
its area for a given n.
A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon
and appending 1-interesting polygons to its rim side by side. You can see the
1-, 2- and 3-interesting polygons in the picture below.

Example
For n = 1, the output should be 1;
For n = 2, the output should be 5;
For n = 3, the output should be 13.
"""


def shape_area(n):
    return 2 * (n - 1) * n + 1


assert shape_area(2) == 5
assert shape_area(3) == 13
assert shape_area(1) == 1
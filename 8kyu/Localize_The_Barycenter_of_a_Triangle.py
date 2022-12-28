"""
The medians of a triangle are the segments that unit the vertices with the
midpoint of their opposite sides. The three medians of a triangle intersect
at the same point, called the barycenter or the centroid. Given a triangle,
defined by the cartesian coordinates of its vertices we need to localize its
barycenter or centroid.

The function bar_triang() or barTriang or bar-triang, receives the coordinates
of the three vertices A, B and C  as three different arguments and outputs
the coordinates of the barycenter O in an array [xO, yO]

This is how our asked function should work: the result of the coordinates
should be expressed up to four decimals, (rounded result).
"""
"""
def bar_triang(a, b, c):
    return [round(sum(x)/3.0, 4) for x in zip(a, b, c)]
"""


def bar_triang(point_a, point_b, point_c):
    x0 = round((point_a[0] + point_b[0] + point_c[0]) / 3, 4)
    y0 = round((point_a[1] + point_b[1] + point_c[1]) / 3, 4)
    return [x0, y0]

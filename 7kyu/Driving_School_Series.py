"""
Every month, a random number of students take the driving test at Fast &
Furious (F&F) Driving School. To pass the test, a student cannot accumulate
more than 18 demerit points.

At the end of the month, F&F wants to calculate the average demerit points
accumulated by ONLY the students who have passed, rounded to the nearest
integer.
"""


def passed(lst):
    points = [x for x in lst if x <= 18]
    if not points:
        return 'No pass scores registered.'
    return round(sum(points) / len(points))

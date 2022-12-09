"""
A high school has a strange principal. On the first day, he has his students
perform an odd opening day ceremony:

There are number of lockers "n" and number of students "n" in the school.
The principal asks the first student to go to every locker and open it.
Then he has the second student go to every second locker and close it.
The third goes to every third locker and, if it is closed, he opens it,
and if it is open, he closes it. The fourth student does this to every fourth
locker, and so on. After the process is completed with the "n"th student,
how many lockers are open?
"""


def num_of_open_lockers(n):
    return int(n ** 0.5)


assert num_of_open_lockers(1) == 1
assert num_of_open_lockers(4) == 2
assert num_of_open_lockers(56) == 7

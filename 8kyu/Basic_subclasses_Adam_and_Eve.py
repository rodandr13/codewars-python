"""
According to the creation myths of the Abrahamic religions, Adam and Eve were
the first Humans to wander the Earth.

You have to do God's job. The creation method must return an array of length 2
containing objects (representing Adam and Eve). The first object in the array
should be an instance of the class Man. The second should be an instance
of the class Woman. Both objects have to be subclasses of Human. Your job
is to implement the Human, Man and Woman classes.
"""
"""
def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass
"""


class Human:
    def __init_(self):
        pass


class Man(Human):
    def __init__(self, name):
        self.name = name


class Woman(Human):
    def __init__(self, name):
        self.name = name


def God():
    Adam = Man("Adam")
    Eva = Woman("Eva")
    return [Adam, Eva]

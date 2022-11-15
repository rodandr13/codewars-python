"""
Ahoy matey!

You are a leader of a small pirate crew. And you have a plan. With the help
of OOP you wish to make a pretty efficient system to identify ships with
a heavy booty on board.

Unfortunately for you, people weigh a lot these days, so how do you know if
a ship is full of gold and not people?
"""


class Ship:

    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        if self.draft - self.crew*1.5 > 20:
            return True
        else:
            return False


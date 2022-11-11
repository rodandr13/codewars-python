"""
You are creating a text-based terminal version of your favorite board game.
In the board game, each turn has six steps that must happen in this order:
roll the dice, move, combat, get coins, buy more health, and print status.
"""

from preloaded import *

health = 100
position = 0
coins = 0


def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()

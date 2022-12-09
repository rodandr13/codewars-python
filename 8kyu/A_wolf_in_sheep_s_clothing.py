"""
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"
"""


def warn_the_sheep(queue):
    queue.reverse()
    if queue[0] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        index_wolf = queue.index("wolf")
        return f"Oi! Sheep number {index_wolf}! You are about to be eaten by a wolf!"

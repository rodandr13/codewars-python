"""
Description:
Remove all exclamation marks from the end of sentence.

Examples
remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"
"""


def remove(s):
    last_word = s.split()[-1][::-1].strip()
    counter = 0
    for char in last_word:
        if char == "!":
            counter += 1
        else:
            break
    return s[:counter * -1] if counter != 0 else s

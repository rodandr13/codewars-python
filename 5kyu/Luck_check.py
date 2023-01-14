def luck_check(string):
    if not isinstance(int(string), int) and not string.isdigit():
        return False
    i, j, total = 0, len(string) - 1, 0
    while i != j and i < j:
        total += (int(string[i]) - int(string[j]))
        i += 1
        j -= 1
    return total == 0

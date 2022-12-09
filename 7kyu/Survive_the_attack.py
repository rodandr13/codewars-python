"""
def is_defended(atks, defs):
    atkPow, defPow = sum(atks),sum(defs)
    survivors = len(defs) - len(atks) + sum((a>b)-(a<b) for a,b in zip(defs,atks))
    return survivors>0 if survivors else defPow>=atkPow
"""


def is_defended(attackers, defenders):
    count_at = 0
    count_def = 0
    min_len = min(len(attackers), len(defenders))
    for i in range(min_len):
        if attackers[i] > defenders[i]:
            count_at += 1
        elif attackers[i] < defenders[i]:
            count_def += 1
    if len(attackers) != len(defenders) and len(attackers) > len(defenders):
        count_at += len(attackers) - len(defenders)
    else:
        count_def += len(defenders) - len(attackers)
    if count_at == count_def:
        return sum(attackers) <= sum(defenders)
    return count_at < count_def

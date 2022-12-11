"""
Everybody knows a little german, right? But remembering the correct articles
is a tough job. Write yourself a little helper, that returns the noun with
the matching article:

each noun containing less than 2 vowels has the article "das"
each noun containing 2/3 vowels has the article "die"
each noun containing more than 3 vowels has the article "der"
Caution: Vowels are "a,e,i,o,u". Umlaute (ä ö ü) are also being counted!
"""
"""
def der_die_das(wort):
    a = sum(x in "aAeEiIoOuUäöü" for x in wort)
    return f'{"das" if a < 2 else "die" if a < 4 else "der"} {wort}'
"""


def der_die_das(wort):
    vowels = "aäeioöuü"
    count_vowels = 0
    for char in wort.lower():
        if char in vowels:
            count_vowels +=1
    if count_vowels < 2:
        return "das " + wort
    elif count_vowels in (2, 3):
        return "die " + wort
    return "der " + wort

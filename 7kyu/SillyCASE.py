"""
Create a function that takes a string and returns that string with the first
half lowercased and the last half uppercased.

eg: foobar == fooBAR

If it is an odd number then 'round' it up to find which letters to uppercase.
See example below.

sillycase("brian")
//         --^-- midpoint
//         bri    first half (lower-cased)
//            AN second half (upper-cased)
"""


def sillycase(silly):
    str_len = len(silly)
    count = str_len // 2 + 1 if str_len % 2 != 0 else str_len // 2
    return silly[:count].lower() + silly[count:].upper()

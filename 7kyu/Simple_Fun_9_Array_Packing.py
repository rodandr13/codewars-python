"""
You are given an array of up to four non-negative integers, each less than 256.
Example
For a = [24, 85, 0], the output should be 21784
An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.

After packing these into one number we get 00000000 01010101 00011000 (spaces
are placed for convenience), which equals to 21784.
"""
"""
def array_packing(arr):
    return int.from_bytes(arr, 'little')
"""


def array_packing(arr):
    arr_bin = [bin(i)[2:] for i in arr]
    temp = []
    for num in arr_bin:
        length = len(num)
        temp.append((8 - length) * '0' + num)
    temp = temp[::-1]

    return int(''.join(temp), 2)

def array_previous_less(arr):
    result = [-1]
    for i in range(1, len(arr)):
        temp = arr[:i]
        while len(temp) != 0:
            last = temp.pop()
            if last < arr[i]:
                result.append(last)
                break
        else:
            result.append(-1)

    return result

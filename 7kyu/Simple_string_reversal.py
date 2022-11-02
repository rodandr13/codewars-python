def solve(s):
    result = [char for char in s[::-1] if char != ' ']
    for i in range(len(s)):
        if s[i] == ' ':
            result.insert(i, ' ')
    return ''.join(result)


assert solve("codewars") == "srawedoc"
assert solve("your code") == "edoc ruoy"
assert solve("your code rocks") == "skco redo cruoy"
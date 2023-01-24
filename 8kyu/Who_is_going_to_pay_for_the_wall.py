def who_is_paying(name):
    if len(name) <= 2:
        return [name]
    return [name, name[:2]]

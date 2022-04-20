def super_in(dictionary, s):
    for x, y in dictionary.items():
        if s == x or s == y:
            return True
    return False

print(super_in({'foo': 'bar', 'accra': 'harmattan', 'olive': 'popeye'}, 'popeye'))
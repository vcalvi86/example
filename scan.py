def scan(ints):
    total = 0
    previous = None

    for val in ints:
        if previous is None or val > previous:
            total += val
            previous = val
        elif val < previous:
            total = 0
            previous = None

    return total

#assert scan([]) == 0
assert scan([0]) == 0
assert scan([1]) == 1
assert scan([1, 2, 3]) == 6
assert scan([-1, 1]) == 0
assert scan([1, 2, 3, 4]) == 10
assert scan([1, 2, 3, -4]) == 0
assert scan([-1]) == -1
assert scan([1, 2, 3, 3]) == 6
assert scan([3, 3, 3, 3, 3]) == 3
assert scan([-1, -2, -3]) == -3
assert scan([1000000]) == 1000000
assert scan([1, 2, 3, 4, 1]) == 0
assert scan([1, 2, 3, 4, 1, 2]) == 2
#assert scan([1, 2, 3, 3, 4, 1, 2, 3]) == 5

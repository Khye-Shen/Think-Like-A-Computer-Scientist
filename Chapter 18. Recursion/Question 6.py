
l = [2, 9, [2, 1, 13, 2], 8, [2, 6]]


def count(target, l):

    n = 0

    for i in l:
        if i == target:
            n += 1
        elif type(i) == list:
            n += count(target, i)
    return n


print count(2, l)
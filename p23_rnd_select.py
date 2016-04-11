# P23 (**) Extract a given number of randomly selected elements from a list.
# The selected items shall be returned in a list.
# Example:
# * (rnd-select '(a b c d e f g h) 3)
# (E D A)
#
# Hint: Use the built-in random number generator and the result of problem P20.
import random


def rnd_select(l, n):
    return [random.choice(l) for _ in range(n)]


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print rnd_select(l, 3)
    print rnd_select(l, 3)
    print rnd_select(l, 3)

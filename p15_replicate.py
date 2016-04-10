# P15 (**) Replicate the elements of a list a given number of times.
# Example:
# * (repli '(a b c) 3)
# (A A A B B B C C C)
import test_utils
from p07_flatten import flatten


def repli(l, n):
    return flatten(map(lambda x: [x] * n, l))


if __name__ == '__main__':
    test_utils.unit_test(repli, ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], ['a', 'b', 'c'], 3)

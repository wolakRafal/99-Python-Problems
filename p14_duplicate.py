# P14 (*) Duplicate the elements of a list.
# Example:
# * (dupli '(a b c c d))
# (A A B B C C C C D D)
from p07_flatten import flatten
import test_utils

def dupli(l):
    return flatten(map(lambda x: [x] * 2, l))


if __name__ == '__main__':
    test_data = ['a', 'b', 'c', 'c', 'd']
    expected = ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']
    test_utils.test(dupli, test_data, expected)
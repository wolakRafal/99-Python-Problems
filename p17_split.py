# P17 (*) Split a list into two parts; the length of the first part is given.
# Do not use any predefined predicates.
#
# Example:
# * (split '(a b c d e f g h i k) 3)
# ( (A B C) (D E F G H I K))
from test_utils import unit_test


def split(list, n):
    """Split a list into two parts; the length of the first part is given in 'n'. """
    return (list[:n], list[n:])


if __name__ == '__main__':
    input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']
    n = 3
    expected = (['a', 'b', 'c'], ['d', 'e', 'f', 'g', 'h', 'i', 'k'])
    unit_test(split, expected, input_list, 3)

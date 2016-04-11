# P18 (**) Extract a slice from a list.
# Given two indices, I and K, the slice is the list containing the elements between
# the I'th and K'th element of the original list (both limits included). Start counting the elements with 1.
#
# Example:
# * (slice '(a b c d e f g h i k) 3 7)
# (C D E F G)
from test_utils import unit_test


def slice(l, i, k):
    return l[i-1:k]


if __name__ == '__main__':
    input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']
    i = 3
    k = 7
    expected = ['c', 'd', 'e', 'f', 'g']
    unit_test(slice, expected, input_list, i, k)

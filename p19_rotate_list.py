# P19 (**) Rotate a list N places to the left.
# Examples:
# * (rotate '(a b c d e f g h) 3)
# (D E F G H A B C)
#
# * (rotate '(a b c d e f g h) -2)
# (G H A B C D E F)
#
# Hint: Use the predefined functions length and append, as well as the result of problem P17.
from test_utils import unit_test
from p17_split import split


def rotate(l, n):
    (init, tail) = split(l, n)
    return tail + init


if __name__ == '__main__':
    input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    n = 3
    expected = ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
    unit_test(rotate, expected, input_list, n)

    expected2 = ['g', 'h', 'a', 'b', 'c', 'd', 'e', 'f']
    unit_test(rotate, expected2, input_list, -2)

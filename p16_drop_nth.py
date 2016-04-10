# P16 (**) Drop every N'th element from a list.
# Example:
# * (drop '(a b c d e f g h i k) 3)
# (A B D E G H K)
from test_utils import unit_test


def drop(l, n):
    zipped = zip(l, range(1, len(l) + 1))
    filtered = filter(lambda x: x[1] % n != 0, zipped)
    return map(lambda x: x[0], filtered)


if __name__ == '__main__':
    input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']
    n = 3
    expected = ['a', 'b', 'd', 'e', 'g', 'h', 'k']
    unit_test(drop, expected, input, n)

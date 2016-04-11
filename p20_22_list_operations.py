# P20 (*) Remove the K'th element from a list.
# Example:
# * (remove-at '(a b c d) 2)
# (A C D)
from test_utils import unit_test


def remove_at(l, n):
    l.pop(n - 1)
    return l


# P21 (*) Insert an element at a given position into a list.
# Example:
# * (insert-at 'alfa '(a b c d) 2)
# (A ALFA B C D)
def insert_at(elem, l, pos):
    l.insert(pos - 1, elem)
    return l


# P22 (*) Create a list containing all integers within a given range.
# If first argument is smaller than second, produce a list in decreasing order.
# Example:
# * (range 4 9)
# (4 5 6 7 8 9)
def _range(start, stop):
    return list(range(start, stop, 1))  # builtin function


if __name__ == '__main__':
    input_list = ['a', 'b', 'c', 'd']
    expected = ['a', 'c', 'd']
    unit_test(remove_at, expected, input_list, 2)

    input_list = ['a', 'b', 'c', 'd']
    expected2 = ['a', 'alfa', 'b', 'c', 'd']
    unit_test(insert_at, expected2, 'alfa', input_list, 2)

    unit_test(_range, list(xrange(1, 10, 1)), 1, 10)

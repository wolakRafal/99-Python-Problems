# P07 (**) Flatten a nested list structure.
#     Transform a list, possibly holding lists as elements into a `flat' list by replacing each list with its elements (recursively).
# Example:
# * (my-flatten '(a (b (c d) e)))
# (A B C D E)
# Hint: Use the predefined functions list and append.
import collections
import test_utils


def flat(iterable, x):
    if isinstance(x, collections.Iterable) and not isinstance(x, basestring):
        iterable.extend(flatten(x))
    else:
        iterable.append(x)

    return iterable


def flatten(l):
    return reduce(flat, l, [])


if __name__ == "__main__":
    test_list = [1, [2, [3]], [[[[4, 5]]]]]
    expected = [1, 2, 3, 4, 5]
    test_utils.unit_test(flatten, expected, test_list)

    test_utils.unit_test(flatten, [1, 1, 2, 2, 3, 3], [[1, 1], [2, 2], [3, 3]])

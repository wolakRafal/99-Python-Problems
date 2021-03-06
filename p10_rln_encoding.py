# P10 (*) Run-length encoding of a list.
#     Use the result of problem P09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as lists (N E) where N is the number of duplicates of the element E.
#
#     Example:
# * (encode '(a a a a b c c a a d e e e e))
# ((4 A) (1 B) (2 C) (2 A) (1 D)(4 E))


def count(acc, x):
    """If symbol x exists in acc on last position increase counter, otherwise add new tuple.

        Returns list of pairs: (symbol counter, symbol)"""

    def containSymbol(l, symbol):
        return l[-1][1] == symbol if l else False

    def increaseCounter(l):
        """Increase counter on last element of the list,
        Returns modified list"""
        a = l[-1]
        l[-1] = (a[0] + 1, a[1])
        return l

    return acc + [(1, x)] if not containSymbol(acc, x) else increaseCounter(acc)


def encode(s):
    return reduce(count, s, [])


if __name__ == "__main__":
    test = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
    expected = [(4, 'A'), (1, 'B'), (2, 'C'), (2, 'A'), (1, 'D'), (4, 'E')]
    print "input:", test
    result = map(lambda x: (x[0], x[1].upper()), encode(test))
    print "result:", result
    print "expected result:", expected
    print "Test result:", "pass" if expected == result else "failed"

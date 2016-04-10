# P11 (*) Modified run-length encoding.
# Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as (N E) lists.
#
# Example:
# * (encode-modified '(a a a a b c c a a d e e e e))
# ((4 A) B (2 C) (2 A) D (4 E))
from _codecs import encode

from p10_rln_encoding import encode


def rln_modified(l):
    def foo(tuple):
        return tuple[1] if tuple[0] == 1 else tuple

    return map(foo, encode(l))

if __name__ == '__main__':
    test = map(lambda x: x.upper(), ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e'])
    expected = [(4, 'A'), 'B', (2, 'C'), (2,'A'), 'D', (4, 'E')]
    print "input:", test
    result = rln_modified(test)
    print "result:", result
    print "expected result:", expected
    print "Test result:", "pass" if expected == result else "failed"
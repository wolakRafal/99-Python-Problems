# P12 (**) Decode a run-length encoded list.
# Given a run-length code list generated as specified in problem P11. Construct its uncompressed version.


def _unfold(acc, elem_tuple):
    return acc + [elem_tuple[1]] * elem_tuple[0]


def decode(encoded_msg):
    return reduce(_unfold, encoded_msg, [])
    
    
if __name__ == '__main__':
    test = [(4, 'A'), (1, 'B'), (2, 'C'), (2, 'A'), (1, 'D'), (4, 'E')]
    expected = ['A', 'A', 'A', 'A', 'B', 'C', 'C', 'A', 'A', 'D', 'E', 'E', 'E', 'E']
    print "input:", test
    result = decode(test)
    print "result:", result
    print "expected result:", expected
    print "Test result:", "pass" if expected == result else "failed"
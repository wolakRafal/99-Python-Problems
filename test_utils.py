
def unit_test(function, expected, *test_input):
    print "Input:", test_input
    result = _call_fun(function, test_input)
    print "Result:", result
    print "Expected result:", expected
    print "Test result:", "PASS" if expected == result else "FAILED!"
    return expected == result


def _call_fun(fun, args):
    if len(args) == 1:
        return fun(args[0])
    elif len(args) == 2:
        return fun(args[0], args[1])
    elif len(args) == 3:
        return fun(args[0], args[1], args[2])
    else:
        return fun()

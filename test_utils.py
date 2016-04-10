
def test(function, test_data, expected):
    print "Input:", test_data
    result = function(test_data)
    print "Result:", result
    print "Expected result:", expected
    print "Test result:", "PASS" if expected == result else "FAILED!"

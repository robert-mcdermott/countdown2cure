#!/usr/bin/python
import sys

def test(target):
    if target == 'pass':
        for x in range(1,10):
            print("Test \'%s\': PASS" % x)
        sys.exit(0)

    if target == 'fail':
        for x in range(1,10):
            print("Test \'%s\': FAIL" % x)
        sys.exit(99)

if __name__ == "__main__":
    target = sys.argv[1]
    test(target)

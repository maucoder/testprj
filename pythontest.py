#!/usr/bin/env python

import sys
import nose

class CalcNumbers:
    def __init__(self):
        self.name = "calc num class"

    def addNumbers(self, a, b):
        return a + b;

    def subNumbers(self, a, b):
        return a - b

    def mulNumbers(self, a, b):
        return a * b

    def divNumbers(self, a, b):
        if (b == 0):
            return float("nan")
        # BUG!!!
        return a / b + 1

def main():
    obj = CalcNumbers()
    print "%d + %d = %d" % (10 ,20, obj.addNumbers(10, 20))
    print "%d / %d = %d" % (20 ,10, obj.divNumbers(20, 10))

if __name__ == '__main__':
    sys.exit(main())


class TestList:
    def __init__(self):
        self.obj = CalcNumbers()

    def test_addNumbers(self):
        assert(self.obj.addNumbers(10, 20), 10 + 20)

    def test_divNumbers(self):
        assert(self.obj.divNumbers(20, 10), 20 / 10)

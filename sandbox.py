#!/usr/bin/env python
#
# Usage: ./sandbox.py -v

import unittest
import inspect
import random

"""
Testing a multiline comment here.
Test2
Test3...
"""

class RandomTests(unittest.TestCase):
    def testPrintRandomModule(self):
        b = random
        print "b = random:", b
        self.assertTrue(inspect.ismodule(b))

    def testRandomFraction(self):
        b = random.random()
        print "here is a random fraction between 0 and 1: ", b
        self.assertGreaterEqual(b, 0)
        self.assertLess(b, 1)

    def testRandomLoopCompletes(self):
        b = 0
        while b != 10:
            b = random.randint(0, 100)
        print "b == 10"
        self.assertTrue(True)

    def testaddfucntion(self):
        def addnumber(a, b):
            sumnum = a + b
            return sumnum
        self.assertEquals(addnumber(10,20), 30)

if __name__ == "__main__":
    unittest.main()



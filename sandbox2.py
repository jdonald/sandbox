#!/usr/bin/env python
#
# Usage: ./sandbox2.py -v

import unittest
import inspect
import random

def add_stdin_numbers():
    a = input ("number1")
    b = input ("number2")
    return a + b

def stdin_name_is_pig():
    a = input ( "your name is ")
    print (a + " " + "is a pig")

def last(s):
    return s[-1]

class StringTests(unittest.TestCase):
    def test_list_str_length(self):
        a  = ['aaa','c','dddd','rr']
        b = len(a[0])
        print b
        self.assertEquals(b, 3)

    def test_sorting_via_key(self):
        a = ['aaa','c','dddd','rr']
        a.sort(key=len)
        print a
        self.assertEquals(a[0], 'c')
        self.assertEquals(a[3], 'dddd')

    def test_last(self):
        s = "hello"
        self.assertEquals(last(s), 'o')

    def test_first_two(self):
        def first_two(s):
            return s[0:2]
        s = "goodbye"
        print s + " - " + first_two(s)
        self.assertEquals(first_two(s), 'go')

    def test_sort_custom_key(self):
        def newkey(s):
            return s[1]

        a = ['56', '93', '55']
        a.sort(key=newkey)
        print a
        self.assertEquals(a[1], '55')

    def test_digit_index(self):
        a = 187
        print(str(a)[1])
        self.assertRaises(TypeError, lambda: a[1])
        self.assertEquals(str(a)[1], '8')

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3

import unittest
from func import square


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(square(0), 0)

    def testCase2(self):
        self.assertEqual(square(-1), 1)

    def testCase3(self):
        self.assertEqual(square(5), 25)


if __name__ == '__main__':
    unittest.main()
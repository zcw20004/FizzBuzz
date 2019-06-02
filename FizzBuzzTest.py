#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:hopzheng
@file: FizzBuzzTest.py
@created: 2019/06/02
"""
from FizzBuzz import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):

    def test(self):
        self.fizzBuzz = FizzBuzz(5,5)
        self.assertTrue(self.fizzBuzz.checkFizz())
        self.assertTrue(self.fizzBuzz.checkBuzz())
        self.fizzBuzz = FizzBuzz(18, 23)
        self.assertFalse(self.fizzBuzz.checkFizz())
        self.assertFalse(self.fizzBuzz.checkBuzz())
        self.fizzBuzz = FizzBuzz(0, -1)
        self.assertFalse(self.fizzBuzz.checkFizz())
        self.assertFalse(self.fizzBuzz.checkBuzz())
        self.fizzBuzz = FizzBuzz(3, 5)
        self.assertTrue(self.fizzBuzz.checkFizz())
        self.assertTrue(self.fizzBuzz.checkBuzz())
        self.assertTrue(self.fizzBuzz.say(3) == "Fizz")
        self.assertTrue(self.fizzBuzz.say(5) == "Buzz")
        self.assertTrue(self.fizzBuzz.say(15) == "FizzBuzz")
        self.assertTrue(self.fizzBuzz.say(33) == "Fizz")
        self.assertTrue(self.fizzBuzz.say(53) == "FizzBuzz")
        self.assertTrue(self.fizzBuzz.say(98) == 98)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

import tkinter as tk
import shapely
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestTkBasic(unittest.TestCase):
    def test_constructor(self):
        pass


class TestShapely(unittest.TestCase):
    def test_Point(self):
        actual = shapely.Point(10, 20)
        self.assertEqual(10, actual.x)
        self.assertEqual(20, actual.y)


if __name__ == "__main__":
    unittest.main()

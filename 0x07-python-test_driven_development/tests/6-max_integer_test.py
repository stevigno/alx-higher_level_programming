#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        a = __import__('6-max_integer').__doc__
        self.assertTrue(len(a) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        b = max_integer.__doc__
        self.assertTrue(len(b) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        c = []
        self.assertIsNone(max_integer(c))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        d = [8]
        self.assertEqual(max_integer(d), 8)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        e = [1, 6, 8, 39, 17, 58]
        self.assertEqual(max_integer(e), 58)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        m = [1, 6, 8, 390, 17, 58]
        self.assertEqual(max_integer(m), 390)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        g = [100, 6, 8, 39, 17, 58]
        self.assertEqual(max_integer(g), 100)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        ab = [100, 6, 8, -39, 17, 58]
        self.assertEqual(max_integer(ab), -39)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        bb = [-8, -58, -75, -1, -100]
        self.assertEqual(max_integer(bb), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()

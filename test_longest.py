import unittest
from longest import longest_substring


class Test_Longest_Substring(unittest.TestCase):

    def test_abcabcbb(self):
        self.assertEqual(longest_substring('abcabcbb'), 3)

    def test_bbbbb(self):
        self.assertEqual(longest_substring('bbbbb'), 1)

    def test_pwwkew(self):
        self.assertEqual(longest_substring('pwwkew'), 3)

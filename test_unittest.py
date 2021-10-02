"""Test for module inc_dec with unittest framework."""

import inc_dec    # The code to test
import unittest   # The test framework

"""Class to test increment and decrement functions."""


class TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)


if __name__ == '__main__':
    unittest.main()

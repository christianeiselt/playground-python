"""Test for module inc_dec with unittest framework."""

import unittest   # The test framework
import inc_dec    # The code to test


class TestIncrementDecrement(unittest.TestCase):

    """Class to test increment and decrement functions."""


def test_increment(self):
    """Tests incrementing for number 3."""
    self.assertEqual(inc_dec.increment(3), 4)


def test_decrement(self):
    """Tests decrementing for number 3."""
    self.assertEqual(inc_dec.decrement(3), 2)


if __name__ == '__main__':
    unittest.main()

"""Test for module inc_dec with unittest framework."""

import unittest   # The test framework
import inc_dec    # The code to test

"""Class to test increment and decrement functions."""


class TestIncrementDecrement(unittest.TestCase):
    """Tests incrementing for number 3."""

    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    """Tests decrementing for number 3."""

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)


if __name__ == '__main__':
    unittest.main()

"""Test for module inc_dec with pytest framework."""
import inc_dec    # The code to test


def test_increment():
    """Tests incrementing for number 3."""
    assert inc_dec.increment(3) == 4


def test_decrement():
    """Tests decrementing for number 3."""
    assert inc_dec.decrement(3) == 2

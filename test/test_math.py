from nose.tools import *

from math import (
    gcd
)


class TestStack():
    """
    Test GCD Implementation
    """

    def test_gcd(self):
        self.obj = gcd.GCD()
        assert self.obj.gcd([8, 12, 4]) == 4
        assert self.obj.gcd(8, 16) == 8
        assert self.obj.gcd(8, 16) != 4
        assert_raises(IndexError, self.obj.gcd, 8)
        assert_raises(TypeError, self.obj.gcd, 8, 0)
        assert_raises(TypeError, self.obj.gcd, 0, 0)
        assert_raises(TypeError, self.obj.gcd, 0, 8)

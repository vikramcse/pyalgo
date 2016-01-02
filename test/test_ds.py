from nose.tools import *

from ds import (
	stack
)

class TestStack():
    """
    Test Stack Implementation
    """
    def test_stack(self):
        self.sta = stack.Stack()
        self.sta.add(5)
        self.sta.add(8)
        self.sta.add(10)
        self.sta.add(2)

        assert self.sta.remove() == 2
        assert self.sta.peek() == 10
        assert self.sta.is_empty() == False
        assert self.sta.size() == 3
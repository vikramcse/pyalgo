"""
    Stack
    -----
    A stack or LIFO (last in, first out) is an abstract data type that serves
    as a collection of elements, with two principal operations: push, which
    adds an element to the collection, and pop, which removes the last element
    that was added.
"""
class Node(object):
    """
    An internal class that represents a node with a single item
    and a link to the next node.
    """

    def __init__(self, item):
        self.item = item
        self.next = None

class Stack(object):

    def __init__(self):
        self.head = None
        self._size = 0

    def add(self, value):
        """
        Add element at last
        Time Complexity:  O(1)
        """

        temp = Node(value)
        temp.next = self.head
        self.head = temp;
        self._size = self._size + 1

    def remove(self):
        """
        Remove element from last return value
        Time Complexity:  O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")

        temp = self.head;
        self.head = self.head.next
        self._size = self._size - 1
        return temp.item

    def is_empty(self):
        """
        1 value returned on empty 0 value returned on not empty
        Time Complexity:  O(1)
        """
        return self._size == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        return self.head.item

    def size(self):
        """
        Return size of stack
        Time Complexity:  O(1)
        """
        return self._size

    def __str__(self):
        """
        String representation of the stack.
        """
        return " ".join(reversed([str(item) for item in self]))
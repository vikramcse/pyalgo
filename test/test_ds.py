from ds import (
    stack,
    queue,
    linked_list,
)


class TestStack:
    """
    Test Stack Implementation
    """

    def __init__(self):
        self.sta = stack.Stack()

    def test_stack(self):
        self.sta.add(5)
        self.sta.add(8)
        self.sta.add(10)
        self.sta.add(2)

        assert self.sta.remove() == 2
        assert self.sta.peek() == 10
        assert self.sta.is_empty() == False
        assert self.sta.size() == 3


class TestQueue:
    """
    Test Queue Implementation
    """

    def __init__(self):
        self.queue = queue.Queue()

    def test_queue(self):
        self.queue.isEmpty() == True

        self.queue.enqueue(5)
        self.queue.enqueue(2)
        self.queue.enqueue(1)
        self.queue.enqueue(0)

        assert self.queue.peek() == 5
        assert self.queue.size() == 4

        assert self.queue.dequeue() == 5
        assert self.queue.size() == 3


class TestLinkedList:
    def __init__(self):
        self.ll = linked_list.LinkedList()

        self.ll.append_last(10)
        self.ll.append_last(20)
        self.ll.append_last(30)

    def test_linked_list_print(self):
        assert self.ll.__str__() == '10 20 30'

    def test_linked_list_append_front(self):
        self.ll.append_front('front1')
        assert self.ll.__str__() == 'front1 10 20 30'
        size = self.ll.get_size()
        assert size == 4

        size = self.ll.get_size()
        assert size == 4

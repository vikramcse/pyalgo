from ds import (
    stack,
    queue
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


class TestQueue():
    """
    Test Queue Implementation
    """

    def test_queue(self):
        self.queue = queue.Queue()

        self.queue.isEmpty() == True

        self.queue.enqueue(5)
        self.queue.enqueue(2)
        self.queue.enqueue(1)
        self.queue.enqueue(0)

        assert self.queue.peek() == 5
        assert self.queue.size() == 4

        assert self.queue.dequeue() == 5
        assert self.queue.size() == 3

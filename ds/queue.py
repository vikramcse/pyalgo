class Node(object):
    """
    An internal class that represents a node with a single item
    and a link to the next node.
    """

    def __init__(self, item):
        self.item = item
        self.next = None

class Queue(object):

	def __init__(self):
		self.head = None
		self.rear = None
		self._size = 0

	def size(self):
		"""Get the size of queue."""
		return self._size

	def isEmpty(self):
		"""Chech weather the queue is empty."""
		return self._size == 0

	def enqueue(self, value):
		"""Insert an item to the queue."""
		temp = self.rear # get the last element
		self.rear = Node(value)

		if self.isEmpty():
			self.head = self.rear
		else:
			temp.next = self.rear
		self._size = self._size + 1

	def dequeue(self):
		""" Remove an item form queue"""
		if self.isEmpty():
			raise IndexError("Queue underflow")

		temp = self.head
		self.head = self.head.next
		self._size = self._size - 1
		return temp.item

	def peek(self):
		""" Get the head element of queue."""
		if self.isEmpty():
			raise IndexError("Queue underflow")
		return self.head.item

	def __str__(self):
        """String representation of the queue."""
        return " ".join([str(item) for item in self])

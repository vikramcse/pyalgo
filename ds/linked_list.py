class Node(object):
    """
    An internal class that represents a node with a single item
    and a link to the next node.
    """

    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def append_last(self, value):
        if not value:
            return ValueError('Value must be need to insert into stack')

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def append_front(self, value):
        if not value:
            return ValueError('Value must be need to insert into stack')

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        temp = self.head
        ll_string = ''

        while temp is not None:
            ll_string += str(temp.item) + str(" ")
            temp = temp.next

        return ll_string.strip()

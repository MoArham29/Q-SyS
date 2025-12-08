# QStructure.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        new_node = Node(item)

        # If queue already has elements
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the first item in the queue."""
        if self.head is None:
            return None

        removed = self.head
        self.head = removed.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        return removed.value

    def peek(self):
        """Return first item without removing it."""
        return self.head.value if self.head else None

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0

    def size(self):
        """Return number of items in queue."""
        return self._size

# QStructure.py

class Node:
    """A node in a singly-linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """A queue implemented using a linked list (FIFO)."""
    
    def __init__(self):
        self.head = None   # front of the queue
        self.tail = None   # end of the queue
        self._size = 0

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        Time Complexity: O(1)
        """
        new_node = Node(item)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self._size += 1

    def dequeue(self):
        """
        Remove and return the first item in the queue.
        Time Complexity: O(1)
        """
        if self.head is None:
            return None

        removed_node = self.head
        self.head = removed_node.next

        if self.head is None:
            self.tail = None  # queue is now empty

        self._size -= 1
        return removed_node.value

    def peek(self):
        """Return the item at the front without removing it. O(1)."""
        return self.head.value if self.head else None

    def is_empty(self):
        """Return True if the queue contains no elements."""
        return self._size == 0

    def size(self):
        """Return the number of items in the queue."""
        return self._size

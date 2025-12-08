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
        """Adding to the end of the queue."""
        new_node = Node(item)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and send the first item in the Q."""
        if self.head is None:
            return None

        removed = self.head
        self.head = removed.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        return removed.value

    def peek(self):
        """Send first item without deleting it."""
        return self.head.value if self.head else None

    def is_empty(self):
        """Checking if Q is empty."""
        return self._size == 0

    def size(self):
        return self._size

# mediStat/structures.py

from collections import deque

class Stack:
    """
    A simple LIFO stack using a Python list.
    """

    def __init__(self):
        self._data = []

    def push(self, item):
        """
        Push an item onto the top of the stack.
        """
        self._data.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()

    def peek(self):
        """
        Return the top item without removing it, or None if empty.
        """
        return self._data[-1] if not self.is_empty() else None

    def is_empty(self):
        """
        Return True if the stack is empty.
        """
        return len(self._data) == 0

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self._data)

    def __iter__(self):
        """
        Iterate from top of stack to bottom.
        """
        return reversed(self._data)

    def __repr__(self):
        return f"Stack({self._data!r})"


class Queue:
    """
    A simple FIFO queue using collections.deque.
    """

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        """
        self._data.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._data.popleft()

    def peek(self):
        """
        Return the front item without removing it, or None if empty.
        """
        return self._data[0] if not self.is_empty() else None

    def is_empty(self):
        """
        Return True if the queue is empty.
        """
        return len(self._data) == 0

    def size(self):
        """
        Return the number of items in the queue.
        """
        return len(self._data)

    def __iter__(self):
        """
        Iterate from front of queue to back.
        """
        return iter(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)!r})"

from collections import deque

class Stack:
    """
    A simple LIFO stack using a Python list.
    """

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __iter__(self):
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
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._data.popleft()

    def peek(self):
        return self._data[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)!r})"

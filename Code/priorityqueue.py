#!python

from binaryheap import BinaryMinHeap


class PriorityQueue(object):
    """PriorityQueue: a partially ordered queue with methods to enqueue items
    in priority order and to access and dequeue its highest priority item.
    Item pairs are stored in a binary min heap for its efficient operations."""

    def __init__(self):
        """Initialize this priority queue."""
        # Initialize new binary min heap to store items in this priority queue
        self.heap = BinaryMinHeap()
        # Initialize new dictionary to store priority (key) and item (value)
        self.priority_dict = {}

    def __repr__(self):
        """Return a string representation of this priority queue."""
        return 'PriorityQueue({} items, front={})'.format(self.size(), self.front())

    def is_empty(self):
        """Return True if this priority queue is empty, or False otherwise."""
        return self.heap.is_empty()

    def length(self):
        """Return the number of items in this priority queue."""
        return self.heap.size()

    def enqueue(self, item, priority):
        """Insert the given item into this priority queue in order according to
        the given priority."""
        """For time complexity, see binaryheap.py insert() analysis. 
        Other operations in this method require O(1) time."""
        # DONE: Insert given item into heap in order according to given priority
        self.heap.insert(priority)
        self.priority_dict[priority] = item

    def front(self):
        """Return the item at the front of this priority queue without removing
        it, or None if this priority queue is empty."""
        """For time complexity, see binaryheap.py get_min() analysis. 
        Other operations in this method require O(1) time."""
        if self.size() == 0:
            return None
        # DONE: Return minimum item from heap
        top_priority = self.heap.get_min()
        return self.priority_dict[top_priority]

    def dequeue(self):
        """Remove and return the item at the front of this priority queue,
        or raise ValueError if this priority queue is empty."""
        """For time complexity, see binaryheap.py delete_min() analysis. 
        Other operations in this method require O(1) time."""
        if self.size() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # DONE: Remove and return minimum item from heap
        top_priority = self.heap.delete_min()
        return self.priority_dict.pop(top_priority)

    def push_pop(self, item, priority):
        """Remove and return the item at the front of this priority queue,
        and insert the given item in order according to the given priority.
        This method is more efficient than calling dequeue and then enqueue."""
        """For time complexity, see binaryheap.py replace_min() analysis. 
        Other operations in this method require O(1) time."""
        if self.size() == 0:
            raise ValueError('Priority queue is empty and has no front item')
        # DONE: Replace and return minimum item from heap
        top_priority = self.heap.replace_min(priority)
        self.priority_dict[priority] = item
        return self.priority_dict.pop(top_priority)

#!python

from binaryheap import BinaryMinHeap

def heap_sort(items):
    """Sort given items by using a binary heap structure for ordering.
    DONE: Running time: O(n^2), since the algorithm iterates through n items n times each.
    DONE: Memory usage: O(1), since the input array is modified in-place."""
    # Build a binary min heap with the given items
    min_heap = BinaryMinHeap(items)
    sorted_list = []
    # Append the smallest item remaining in the binary heap to the sorted list
    while not min_heap.is_empty():
        sorted_list.append(min_heap.delete_min())
    # Re-populate the original list with the sorted list for testing purposes
    for i in range(len(items)):
        items[i] = sorted_list[i]

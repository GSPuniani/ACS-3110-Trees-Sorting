#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    DONE: Running time: O(n), because the worst-case scenario would require 
    iterating through the entire array once.
    DONE: Memory usage: O(n), because the worst-case scenario would require 
    iterating through the entire array once."""
    # DONE: Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True

unordered_items = [3, 15, 4, 7, 20, 6, 18, 11, 9, 7] # Should return False
ordered_items = [3, 4, 6, 7, 7, 9, 11, 18, 20] # Should return True
print(is_sorted(unordered_items))
print(is_sorted(ordered_items))


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

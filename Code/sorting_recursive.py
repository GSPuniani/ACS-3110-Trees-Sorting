#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?""" 
    sorted_list = []
    i, j = 0, 0
    # DONE: Repeat until one list is empty
    while i < len(items1) and j < len(items2):
        # DONE: Find minimum item in both lists and append it to new list
        if items1[i] <= items2[j]:
            sorted_list.append(items1[i])
            i += 1
        else:
            sorted_list.append(items2[j])
            j += 1
    # DONE: Append remaining items in non-empty list to new list
    if i < len(items1):
        sorted_list.extend(items1[i:])
    elif j < len(items2):
        sorted_list.extend(items2[j:])
    return sorted_list
    

# list1 = [1, 4, 7, 9, 10, 14]
# list2 = [3, 6, 9, 12, 15, 18]
# print(merge(list1, list2))

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each by any non-recursive technique, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    mid_index = len(items) // 2
    first_half = items[:mid_index]
    second_half = items[mid_index:]
    first_half.sort()
    second_half.sort()
    sorted_list = merge(first_half, second_half)
    for i in range(len(items)):
        items[i] = sorted_list[i]

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # DONE: Check if list is so small it's already sorted (base case)
    if len(items) == 1:
        return items
    # DONE: Split items list into approximately equal halves
    mid_index = len(items) // 2
    first_half = items[:mid_index]
    second_half = items[mid_index:]
    # DONE: Sort each half by recursively calling merge sort
    merge_sort(first_half)
    merge_sort(second_half)
    # DONE: Merge sorted halves into one list in sorted order
    sorted_list = merge(first_half, second_half)
    for i in range(len(items)):
        items[i] = sorted_list[i]


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # DONE: Choose a pivot any way and document your method in docstring above
    pivot = items[high]
    i = low
    # DONE: Loop through all items in range [low...high]
    for j in range(low, high):
        # DONE: Move items less than pivot into front of range [low...p-1]
        # DONE: Move items greater than pivot into back of range [p+1...high]
        if items[j] <= pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    # DONE: Move pivot item into final position [p] and return index p
    items[i], items[high] = items[high], items[i]
    return i



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    DONE: Best case running time: O(n log n), where n is the number of items in the list. The best case occurs when the list is already sorted.
    DONE: Worst case running time: O(n^2), where n is the number of items in the list. The worst case occurs when the list is in reverse order.
    DONE: Memory usage: O(1), since the items are sorted in place."""
    # DONE: Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    # DONE: If list or range is so small it's already sorted (base case)
    if high - low <= 1:
        return items
    if low < high:
        # DONE: Partition items in-place around a pivot and get index of pivot
        p = partition(items, low, high)
        # DONE: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p - 1)
        quick_sort(items, p + 1, high)


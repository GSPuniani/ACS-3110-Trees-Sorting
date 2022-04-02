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
    print(first_half)
    second_half.sort()
    print(second_half)
    sorted_list = merge(first_half, second_half)
    return sorted_list

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

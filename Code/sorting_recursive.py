#!python


# ------------------------CHALLENGE 2------------------------


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    DONE: Running time: O(n), since the lists are iterated over and merged in linear time.
    DONE: Memory usage: O(n), since an auxiliary list is created.""" 
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
    DONE: Running time: O(n log n), since that is the time complexity of Timsort (used for both halves).
    DONE: Memory usage: O(n), since an auxiliary list is created."""
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
    DONE: Running time: O(n log n), since the array is recursively split into halves and then merged in linear time.
    DONE: Memory usage: O(n), since an auxiliary list is created."""
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



# ------------------------CHALLENGE 3------------------------

# Class Exercise - NOT USED FOR ACTUAL IMPLEMENTATION
def naive_partition(items):
    """Return index `p` without in-place partitioning (use out-of-place arrays)."""
    pivot = items[0]
    lower_array = []
    higher_array = []
    for item in items:
        if item <= pivot:
            lower_array.append(item)
        else:
            higher_array.append(item)
    return lower_array, higher_array


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (the right-most element) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    DONE: Running time: O(n), since each element is compared to the pivot.
    DONE: Memory usage: O(1), since the items are sorted in place."""
    # DONE: Choose a pivot by selecting the right-most element
    pivot = items[high]
    p = low
    # DONE: Loop through all items in range [low...high]
    for i in range(low, high):
        # DONE: Move items less than pivot into front of range [low...p-1]
        # DONE: Move items greater than pivot into back of range [p+1...high]
        if items[i] <= pivot:
            items[p], items[i] = items[i], items[p]
            p += 1
    # DONE: Move pivot item into final position [p] and return index p
    items[p], items[high] = items[high], items[p]
    return p



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    DONE: Best case running time: O(n log n). The best case occurs when the list is already sorted. 
    Every element would be compared log n times due to balanced partitions producing even splits.
    DONE: Worst case running time: O(n^2). The worst case occurs when the list is in reverse order. Then 
    every element is compared to every other element n times, so there are n*n calls.
    DONE: Memory usage: O(log n) for the recursive call stack (list roughly halved every time)."""
    # DONE: Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    # DONE: If list is so small it's already sorted (base case)
    if len(items) == 1:
        return items
    if low < high:
        # DONE: Partition items in-place around a pivot and get index of pivot
        p = partition(items, low, high)
        # DONE: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, p - 1)
        quick_sort(items, p + 1, high)


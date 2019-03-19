def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i, arr in enumerate(items):
        try:
            if items[i+1] < arr:
                items[i] = items[i+1]
                items[i+1] = arr
                bubble_sort(items)
        except IndexError:
            pass
    return items



def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    # Cae returns, so if reached then function will terminate after line 8
    if len_i == 1:
        return items
    # Recursive case. Find midpoint of list
    mid_point = int(len_i / 2)
    # divide list into two halves
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    # call merge_sort function on each half of list
    return merge(i1, i2)

# Merge function.
def merge(A, B):
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list



def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    """
    the quick sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    high = []
    low = []
    pivot_list = []

    if len(items) <= 1:
        return items
    else:
        pivot = items[0]
        for i in items:
            if i < pivot:
                low.append(i)
            elif i > pivot:
                high.append(i)
            else:
                pivot_list.append(i)
        high = quick_sort(high)
        low = quick_sort(low)

    return low + pivot_list + high

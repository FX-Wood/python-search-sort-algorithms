def merge_sort(arr):
    print('initial array', arr)
    # split the array
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        # Divide the array in half
        left = arr[:mid]
        right = arr[mid:]
        # call merge_sort on each side
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge(sorted_left, sorted_right)

def merge(left, right):
    print(left, right)
    if len(right) == 0:
        return left
    if len(left) == 0:
        return right
    # start with a value that is going to be lower than lowest possible value
    if left[0] <= right[0]:
        smallest_num = left.pop(0)
    else:
        smallest_num = right.pop(0)
    merged = merge(left, right)
    merged.insert(0, smallest_num)
    return merged
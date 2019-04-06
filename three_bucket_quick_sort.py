def three_bucket_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    mid = []
    right = []

    for item in arr:
        if item < pivot:
            left.append(item)
        if item > pivot:
            right.append(item)
        elif item == pivot:
            mid.append(item)
    return three_bucket_quick_sort(left) + mid + three_bucket_quick_sort(right)
    
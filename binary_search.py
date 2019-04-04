def binary_search(arr, val, start=0, end=None):
    if not end:
        end = len(arr) - 1

    mid = (start + end) // 2

    if start <= end:    
        if val < arr[mid]:
            # search left half
            return binary_search(arr, val, start, mid - 1)

        elif val > arr[mid]:
            # search right half
            return binary_search(arr, val, mid + 1, end)
        else:
            return mid
    else:
        return "go fish"
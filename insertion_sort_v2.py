def insertion_sort_v2(arr):
    i = 1
    while i < len(arr):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
        i += 1
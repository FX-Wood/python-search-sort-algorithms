def partition(arr,left,right):
    pivot = arr[(left + right) // 2]
    i = left
    j = right
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i],arr[j] = arr[j],arr[i]

def quick_sort(arr, left=0, right=None):
    if right == None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr,left, pivot)
        quick_sort(arr, pivot + 1, right)


def bucket_sort_quick_sort(arr):
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
    return bucket_sort_quick_sort(left) + mid + bucket_sort_quick_sort(right)


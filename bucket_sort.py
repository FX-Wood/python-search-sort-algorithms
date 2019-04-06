import math
from insertion_sort import insertion_sort

def bucket_sort(arr):
    if len(arr) < 2:
        return arr
    # pick a number of buckets
    k = ( 1 + len(arr) // 2)
    # make list of buckets
    bucket_arr = [[] for n in range(k)]
    # find maximum
    max_value = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    # sort each element into a bucket
    for j in range(len(arr)):
        # each element goes into a bucket that is its fraction of the maximum
        bucket_number = math.floor(( arr[j] / (max_value + 1) * k ))
        bucket_arr[bucket_number].append(arr[j])

    for arr in bucket_arr:
        insertion_sort(arr)

    output = []
    for bucket in bucket_arr:
        output += bucket
    return output
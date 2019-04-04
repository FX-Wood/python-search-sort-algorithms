def selection_sort(arr):
    # for each element in arr
    for i in range(len(arr)):
        # set minimum at the beginning
        index_of_min = i
        # look for any elements with a lower value
        for j in range(i, len(arr)):
            # if one is found
            if arr[j] < arr[index_of_min]:
            # save its index as the new minimum
                index_of_min = j
        # once the minimum is found
        # swap it with i
        arr[i], arr[index_of_min] = arr[index_of_min], arr[i]
    return arr
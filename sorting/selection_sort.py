def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr = [-1, 3, 5, -3, 20, 3, 6]

print(selection_sort(arr))

# time complexity = 0(n^2)
# space complexity = 0(1)

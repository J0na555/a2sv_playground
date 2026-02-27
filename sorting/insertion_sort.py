def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


arr = [-1, 3, 5, -3, 20, 3, 6]

print(insertion_sort(arr))

# time complexity = 0(n^2)
# space complexity = 0(1)
# stable sorting algorithm


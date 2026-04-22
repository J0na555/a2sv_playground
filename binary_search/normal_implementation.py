A = [-3, -1, 0, 1, 4, 7]

# time  = o(log n)
# space = o(1)

def binary_search(arr, target):
    l, r = 0, len(arr)-1

    while l <=r:
        mid = (l + r) // 2 

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid -1

    return -1

print(binary_search(A, 1))

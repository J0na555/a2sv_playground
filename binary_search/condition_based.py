B = [False, False, False, False, False, True, True, True]

def binary_search_condition(arr):
    l, r = 0, len(arr)-1

    while l < r:
        mid = (l+r) // 2
        
        if arr[mid]:
            r = mid
        else:
            l = mid + 1

    return l

print(binary_search_condition(B))

# time = o(log n)
# space = o(1)

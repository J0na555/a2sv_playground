# time complexity 0(K+N)
# space complexity 0(K)
# this is a great sorting algorithm for arrays that its max number is small

def counting_sort(arr):
    maxx = max(arr)
    count = [0] * (maxx + 1)

    for x in arr:
        count[x] += 1

    i = 0
    for c in range(maxx+1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1

    return arr


arr = [8, 3, 5, 3, 20, 3, 6]

print(counting_sort(arr))



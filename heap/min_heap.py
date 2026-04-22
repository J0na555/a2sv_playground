# time : 0(n), space 0(1)
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq

heapq.heapify(A)

print(A)

# heap push
# time 0(logn)
heapq.heappsuh(A, 4)

# heap pop 
# time 0(logn)

minn = heapq.heappop(A)

print(A, minn)

# heap sort 
# time 0(n logn), space 0(n)
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)

    new_list = [0]*n

    for i in range(n): 
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return new_list

# heap push pop time 0(logn)

heapq.heappushpop(A)

print(A, 99)

# max heap 


B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

n = len(B)

for i in range(n): 
    B[i] = -B[i]

heapq.heapify(B)

print(B) # prints the negative version of all the numbers

leargest = -heapq.heappop(B)

print(leargest) # prints leargest number in the heapq

heapq.heappush(B, -7) # inserts 7 into the max heap 


def binary_search(A, v):
    low = 0
    high = len(A)-1

    while low <= high:
        mid = (low + high) / 2
        if A[mid] == v:
            return mid
        if A[mid] < v:
            low = mid + 1
        else:
            high = mid -1
    return None

A = [1, 2, 3, 4]
v = 3
print binary_search(A, v)

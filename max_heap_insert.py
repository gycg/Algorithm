from math import ceil
def max_heapify(A, i, heap_size):
    l = 2*i+1
    r = 2*i+2
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def heap_maximum(A):
    return A[0]

def heap_extract_max(A, heap_size):
    if heap_size < 1:
        print "heap underflow"
    max = A[0]
    A[0] = A[heap_size-1]
    heap_size -= 1
    max_heapify(A, 0)
    return max

def heap_increase_key(A, i, key):
    if key < A[i]:
        print "new key is smaller than current key"
    A[i] = key
    k = int(ceil(i/2)-1)
    while i > 0 and A[k] < A[i]:
        A[k], A[i] = A[i], A[k]
        i = k
        k = int(ceil(k/2)-1)

def max_heap_insert(A, key, heap_size):
    heap_size = heap_size + 1
    A += [float("-inf")]
    heap_increase_key(A, heap_size - 1, key)

A = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
max_heap_insert(A, 45, len(A))
print A

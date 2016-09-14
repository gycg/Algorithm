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

def build_max_heap(A, heap_size):
    for i in xrange(heap_size/2, -1, -1):
        max_heapify(A, i, heap_size)

def heapsort(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    for i in xrange(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)

A = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
heapsort(A)
print A

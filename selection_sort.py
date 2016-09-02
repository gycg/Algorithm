def selection_sort(a):
    for i in xrange(len(a)-1):
        min = i
        for j in xrange(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        tmp = a[i]
        a[i] = a[min]
        a[min] = tmp
    return a

a = [7, 3, 2, 9, 4]
print selection_sort(a)

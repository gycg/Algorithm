def find_max_subarray(A, low, high):
    left = 0
    right = 0
    sum = float("-inf")
    for i in xrange(low, high):
        current_sum = 0
        for j in xrange(i, high):
            current_sum += A[j]
            if sum < current_sum:
                sum = current_sum
                left = i
                right = j
    return(left, right, sum)
    
A = [0, -1, 3, -4, 6, -1, 4]
print find_max_subarray(A, 0, 7)

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float("-inf")
    sum = 0
    for i in xrange(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float("-inf")
    sum = 0
    for j in xrange(mid+1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return(max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return(low, high, A[low])
    else:
        mid = (low+high)/2
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return(left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return(right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)

A = [0, -1, 3, -4, 6, -1, 4]
print find_maximum_subarray(A, 0, 6)

def find_max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

A = [0, -1, 3, -4, 6, -1, 4]
print find_max_subarray(A)

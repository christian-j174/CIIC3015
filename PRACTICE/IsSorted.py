def IsSorted(A):
    x = None
    if len(A) > 0:
        x = A[0]
    for a in A:
        if x > a:
            return False
        x = a
    return True


print(IsSorted([2, 3, 4, 5]))



def max_slice(A):
    n = len(A)
    print(n)
    result = 0
    for p in range(n):
        print(p)
        for q in range(p, n):
            print(q)
            sum = 0
            for i in range(p, q + 1):
                sum += A[i]
            result = max(result, sum)
    return result

A = [5,-7,3,5,-2,4,-1]
max_slice(A)
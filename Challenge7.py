"""
CountFactors
============

Count factors of given number n.

Write a function:

    def solution(N)

that, given a positive integer N, returns the number of its factors.
For example, given N = 24, the function should return 8, because 24 has 8 factors,
namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.


MinPerimeterRectangle
=====================
The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle
should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.

the function should return 22, as explained above.
"""

def solution(N):
    factors=[]
    for i in range(1,N+1):
        if N % i == 0:
            factors.append(i)
    print(factors)   
    print(len(factors))
    #return len(factors)
    #
    # Include finding the minimal perimeter of any rectangle whose area equals N.
    #
    k = len(factors)

    k = int(k/2)
    if k >= 2:
        min_para = 2 * (factors[k-1] + factors[k])
        print()
        print("Minimal perimeter of the rectangle is:")
        return min_para
    else:
        print(k)
        return 0

solution(30)

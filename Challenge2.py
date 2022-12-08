""" 
An array A consisting of N integers is given. Rotation of the array means that
each element is shifted right by one index, and the last element of the array is moved
to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
(elements are shifted right by one index and 6 is moved to the first place).

Write a function:

    def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

"""

def solution(A, K):
    T = 1
    while T <= K:
        A.insert(0, A[-1])
        A.pop()
        T += 1

    return A


A = [3, 8, 9, 7, 6]
K = 3

#A = [0, 0, 0]
#K = 1

#A = [1, 2, 3, 4]
#K = 4

solution(A,K)
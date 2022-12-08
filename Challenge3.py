"""
A non-empty array A consisting of N integers is given.
The array contains an odd number of elements, and each element of the array can be paired
with another element that has the same value, except for one element that is left unpaired.

Write a function:

    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions,
returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7

"""
import numpy as np

def solution(A):
    res = np.array(A) #need to convert the list to NumPy array
    unique_list = np.unique(res) #using the numpy.unique() method
    print(f"Unique #: {unique_list}")
    count = 0

    for i in unique_list:
        for j in A:
            if i == j:
                count += 1
                if count >= 2:
                    while j in A:
                        A.remove(j) # removes all instances of j
                        count = 0
    return A
                    

A = [9,3,9,3,9,7,9]
solution(A)

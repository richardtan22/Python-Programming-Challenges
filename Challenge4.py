"""
MaxProductOfThree

Write a function:

    def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Your goal is to find the maximal product of any triplet.
"""

def max_prodt(A):
    sorted_revNums = sorted(A, reverse=True)
    print(sorted_revNums)
    B = sorted_revNums[0]*sorted_revNums[1]*sorted_revNums[2]
    
    return B


    

A = [-3,1,2,-2,5,6]
max_prodt(A)

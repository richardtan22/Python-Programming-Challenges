"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros
that is surrounded by ones at both ends in the binary representation of N.

Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
"""
def binRep(N):
    N1 = str(N) # converting to string
    if N1[-1]=="0" or "0" not in N1:
        print("There is no binary gaps.")
        return 0
    else:
        max_zero = 0
        count_zero = 0
        for i in N1:
            if i == "1":
                count_zero = 0 # reset counter
                #continue
            else:
                count_zero += 1
                max_zero = max(max_zero, count_zero)
                #if count_zero > max_zero:
                    #max_zero = count_zero
                
        return max_zero
        
    

#decNum = 1041000105
decNum = 1041
binNum = bin(decNum)[2:] # type is string
#binNum = 1000111101100000001 # type is int

print(binNum)
print(type(binNum))

binRep(binNum)
"""
Write a function:
    def solution(A, B, P)

with the given A, B and P below and return with the expected result for each of the condition.

Conditions:
    # should return "pom"
    A1 = ["pim","pom"]
    B1 = ["999999999","777888999"]
    P1 = "88999"

    # should return "ann" bcos "ann" is alphabetically smaller than
    # "michael" and "sander".
    A1 = ["sander", "amy", "ann", "michael"]
    B1 = ["123456789", "234567890", "789123456", "123123123"]
    P1 = "1"

    # should return "NO CONTACT"
    A1 = ["adam", "eva", "leo"]
    B1 = ["121212121", "111111111", "444555666"]
    P1 = "112"
"""
def solution(A, B, P):
    n = len(A)
    
    # Contruct a Dictionary using A and B
    C ={} # empty dictionary
    for i in range(n):
        C.update({A[i]:B[i]}) # there is no append in dict, use update instead
    
    # Sort the dictionay key-value
    from collections import OrderedDict
    sorted_C = OrderedDict(sorted(C.items()))

    # Look for P
    for i in sorted_C:
        if P in sorted_C[i]:
            return i
    return "NO CONTACT"

        

A1 = ["sander", "amy", "ann", "michael"]
B1 = ["123456789", "234567890", "789123456", "123123123"]
P1 = "1"

solution(A1, B1, P1) 
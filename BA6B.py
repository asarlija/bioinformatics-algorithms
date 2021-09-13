"""
A solution to a Rosalind bioinformatics problem
Problem Title: Compute the Number of Breakpoints in a Permutation
Rosalind ID: BA6B
URL: http://rosalind.info/problems/ba6b/
"""

def NumberofBreakpoints(str_permutation):
    n=len(str_permutation.split(" "))
    helper="0 "+str_permutation[1:-1]+" "+str(n+1)
    int_permutation=[int(x) for x in helper.split(" ")]
    count=0
    for i in range(0,n+1):
        if int_permutation[i+1]-int_permutation[i]!=1:
            count+=1
    return count
    
str_permutation="(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"
result=NumberofBreakpoints(str_permutation)
print(result)

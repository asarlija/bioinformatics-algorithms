"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement GreedySorting to Sort a Permutation by Reversals
Rosalind ID: BA6A
URL: http://rosalind.info/problems/ba6a/
"""

def GreedySorting(str_permutation):
    helper=[int(x) for x in str_permutation[1:-1].split()]
    S=[]
    for i in range(0,len(helper)):
        if helper[i]==i+1:
            continue
        idx=i
        while True:
            if helper[idx]==i+1 or helper[idx]==-(i+1):
                break
            idx=idx+1
        mid=[-1*x for x in helper[i:(idx+1)]][::-1]
        helper=helper[:i]+mid+helper[(idx+1):]
        S.append(helper.copy())
        if helper[i]<0:
            helper[i]=abs(helper[i])
            S.append(helper.copy())
    if S==[]:
        S=[helper]
    return S

def f(x):
    if x>=0:
        s="+"
    else:
        s=""
    return s

def permPrint(L):
    for i in range(0,len(L)):
        string="(" + " ".join([f(x)+str(x) for x in L[i]]) + ")"
        print(string)
 
str_permutation="(-3 +4 +1 +5 -2)"
L=GreedySorting(str_permutation)
permPrint(L)


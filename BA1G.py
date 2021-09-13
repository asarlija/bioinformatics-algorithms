"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Compute the Hamming Distance Between Two Strings
Rosalind ID: BA1G
URL: http://rosalind.info/problems/ba1g/

Hamming Distance Problem
Compute the Hamming distance between two DNA strings.
Given: Two DNA strings.
Return: An integer value representing the Hamming distance.
"""

def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1
    
    dist = 0
    """ zip(AB,CD) returns (('A','C'),('B','D')) """
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist

x="""GGGCCGTTGGT
GGACCGTTGAC"""
inlines=x.split("\n")
p=inlines[0]
q=inlines[1]
result=HammingDistance(p,q)
print(result)

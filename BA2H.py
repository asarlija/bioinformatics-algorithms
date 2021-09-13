"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement DistanceBetweenPatternAndStrings
Rosalind ID: BA2H
URL: http://rosalind.info/problems/ba2h/
"""
def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1
    dist = 0
    #zip(AB,CD) gives (('A','C'),('B','D'))
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1
    return dist

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def DistanceBetweenPatternAndStrings(pattern, dnalist):
    k=len(pattern)
    dist=0
    for dna in dnalist:
        hamming_distance=len(pattern)+1
        for pattern2 in Lwindows(dna,k):
            if (hamming_distance>HammingDistance(pattern, pattern2)):
                hamming_distance=HammingDistance(pattern, pattern2)
        dist=dist + hamming_distance
    return dist

x='''AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'''
inlines=x.split()
pattern=inlines[0]
dnalist=list()
for i in range(1,len(inlines)):
    dnalist.append(inlines[i])
result=DistanceBetweenPatternAndStrings(pattern,dnalist)
print(result)

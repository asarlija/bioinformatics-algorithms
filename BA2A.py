"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement MotifEnumeration
Rosalind ID: BA2A
URL: http://rosalind.info/problems/ba2a/
"""

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def HammingDistance(p, q):
    """Computes the Hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1
    dist = 0
    #zip(AB,CD) gives (('A','C'),('B','D'))
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1
    return dist

def kmersfrequency(text, k):
    """ returns dictionary of k-mers in text with number of occurrances"""
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return(D)

def ApproximatePatternCount(text,pattern,d):
    """ returns number of occurrances pattern in text with at most
        d mismatches """
    count=0
    nt=len(text)
    np=len(pattern)
    for i in range (0,nt-np+1):
        pattern2=kmer(text,i,np)
        if (HammingDistance(pattern,pattern2)<=d):
            count=count+1
    return count


def suffix(pattern):
    """ substring of pattern without first letter """
    return pattern[1:]

def Neighbours(pattern,d):
    """ returns set of pattern with at most d mismatches """
    nucleotides={'A','C','G','T'}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucleotides
    neighborhood=set()
    suffixNeighbors=Neighbours(suffix(pattern),d)
    for x in suffixNeighbors:
        if (HammingDistance(suffix(pattern),x)<d):
            for n in nucleotides:
                neighborhood.add(n+x)
        else:
            neighborhood.add(pattern[0]+x)
    return neighborhood

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def kmerswithapproxcount(text,k,d):
    """ for given text and integers k (for kmer) and d (for mismatches)
        we return dictionary D
        we slide a window of text length k,
        then we look all Neighbours (pattern) - of what window with d mismatches,
        and we will put a key pattern with value number of occurrances
        that pattern in text with at most
        d mismatches
    """
    
    D=dict()
    for window in Lwindows(text,k):
        for pattern in Neighbours(window,d):
            D[pattern]=ApproximatePatternCount(text,pattern,d)
    return D
    """
        without function subset  
    """

def MotifEnumeration(dnalist,k,d):
    L=list()
    for dna in dnalist:
        L.append(kmerswithapproxcount(dna,k,d))
    RES=dict()
    for D in L:
        for k in D.keys():
            try:
                RES[k]=RES[k]+1
            except KeyError:
                RES[k]=1
    return [k for k,v in RES.items() if v==len(dnalist)]

x="""
3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT
"""
inlines=x.split()
k=int(inlines[0])
d=int(inlines[1])
dnalist=list()
for i in range(2,len(inlines)):
    dnalist.append(inlines[i])
result=MotifEnumeration(dnalist,k,d)
print(result)

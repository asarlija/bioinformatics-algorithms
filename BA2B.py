"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Median String
Rosalind ID: BA2B
URL: http://rosalind.info/problems/ba2b/
"""

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def kmersfrequency(text, k):
    """ for given text and k returns dictionary where key is all k-mers in text
        and value is number of occurrances"""
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return(D)

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

def minHamm(text,pattern):
    """Find minimum Hamming distance between
       Pattern and any k-mer in text"""
    D=kmersfrequency(text,len(pattern))
    return (min([(HammingDistance(pattern,x)) for x in D.keys()]))

def suffix(pattern):
    """ substring of pattern without first letter """
    return pattern[1:]

def Neighbors(pattern,d):
    nucleotides={'A','C','G','T'}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucleotides
    neighborhood=set()
    suffixNeighbors=Neighbors(suffix(pattern),d)
    for x in suffixNeighbors:
        if (HammingDistance(suffix(pattern),x)<d):
            for n in nucleotides:
                neighborhood.add(n+x)
        else:
            neighborhood.add(pattern[0]+x)
    return neighborhood

def kmerNeighbors(text,k):
    """Find all k-mers (words) and their Neighbours in a
        string text together with a minimal hamming distance
        between neighbours and the set of original k-mers"""
    L=set()
    for i in range(0,len(text)-k+1):
        for d in range(0,k+1):
            L.update(Neighbors(kmer(text,i,k),d))
    D=dict()
    for element in L:
        D[element]=minHamm(text,element)
    return D

def MedianString(dnalist,k):
    """Find k-mer Pattern that minimizes
    d(Pattern,Dnalist)=sum(d(Pattern,Dna)) over all k-mers
    Pattern and Dnalist where d=minhamm"""
    L=[]
    setofkeys=set()
    for dna in dnalist:
        L.append(kmerNeighbors(dna,k))
    for element in L: 
        for key in element.keys():
            setofkeys.add(key)
    RES=dict()
    for key in setofkeys: 
        RES[key]=0
    for D in L: 
        for key, value in D.items():
            RES[key]=RES[key]+value
    mincount=min([value for value in RES.values()])
    listresult=[key for key, value in RES.items() if mincount==value] 
    """ if there are multiple results i will take first"""
    return listresult[0]

x = '''3
AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTACGGGACAG'''
inlines=x.split()
k=int(inlines[0])
dnalist=list()
for i in range(1,len(inlines)):
    dnalist.append(inlines[i])
result=MedianString(dnalist,k)
print(result)


 

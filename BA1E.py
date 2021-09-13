"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find Patterns Forming Clumps in a String
Rosalind ID: BA1E
URL: http://rosalind.info/problems/ba1e/

Clump Finding Problem
Find patterns forming clumps in a string.
Given: A string Genome, and integers k, L, and t.
Return: All distinct k-mers forming (L, t)-clumps in Genome.
"""

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return(D)

def kmerfrequency_t(Dict,t):
    """search for all kmers which appears at least t times"""
    reduced_dictionary=list()
    for x in Dict:
        if (Dict[x]>=t):
            reduced_dictionary.append(x)
    return (reduced_dictionary)

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def clump(text,k,L,t):
    """set of all (L,t)-clumps in text"""
    result=set()
    listofwindows=Lwindows(text,L)
    for window in listofwindows:
        Dict=kmersfrequency(window,k)
        reduced_dictionary=kmerfrequency_t(Dict,t)
        for pattern in reduced_dictionary:
            result.add(pattern)
    return result

x="""CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
5 75 4"""
inlines=x.split()
print(inlines)
genome=inlines[0]
k=int(inlines[1])
L=int(inlines[2])
t=int(inlines[3])
result=clump(genome,k,L,t)
print(result)



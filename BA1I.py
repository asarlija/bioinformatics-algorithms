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

def FrequentWordswithMismatches(text,k,d):
    D=kmerswithapproxcount(text,k,d)
    maximum=max(D.values())
    return [key for key,value in D.items() if value==maximum]

x="""ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1"""
inlines=x.split()
text=inlines[0]
k=int(inlines[1])
d=int(inlines[2])
result=FrequentWordswithMismatches(text,k,d)
print(" ".join(result))

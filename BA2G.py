"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement GibbsSampler
Rosalind ID: BA2G
URL: http://rosalind.info/problems/ba2g/
"""
def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def probability(window,profile):
    """ returns number - probability for given kmer and profile matrix """
    p=1
    for i in range (0,len(window)):
        if window[i]=='A':
            p=p*float(profile[0][i])
        if window[i]=='C':
            p = p * float(profile[1][i])
        if window[i] == 'G':
            p = p * float(profile[2][i])
        if window[i] == 'T':
            p = p * float(profile[3][i])
    return p

def MostProbkmerinText(text,k,profile):
    """ returns Profile-most probable kmer in String
        if there are more of them, return just first"""
    D=dict()
    for window in Lwindows(text,k):
        D[window]=probability(window,profile)
    listkmers=[key for key,value in D.items() if value==max(D.values())]
    return listkmers[0]

def count(motifs,nucl,i):
    """compute count for each nucleotide of i-th column"""
    col=[motif[i] for motif in motifs]
    num=0
    if nucl==0:
        num=len([n for n in col if n=='A'])
    if nucl==1:
        num=len([n for n in col if n=='C'])
    if nucl==2:
        num=len([n for n in col if n=='G'])
    if nucl==3:
        num=len([n for n in col if n=='T'])
    return num

def capitalLetter(motifs,i):
    """ find a capital letter of i-th column """
    counts=[count(motifs,nucleotide,i) for nucleotide in range (0,4)]
    maxcount=max(counts)
    listofmaxnucl=[nucleotide for nucleotide in range (0,4) if counts[nucleotide]==maxcount]
    return listofmaxnucl[0]

def score(motifs):
    """ find a number of small letters in motifs"""
    sc=0
    for i in range(0,len(motifs[0])):
        sc=sc+(len(motifs)-count(motifs,capitalLetter(motifs,i),i))
    return  sc

def profileMatrixPseudocounts(motifs,k):
    """ for given set of motifs and k returns profile matrix but with
        pseudocount ! """
    matrix=[]
    for i in range(0,4):
        matrix.append(list())
    for i in range(0,k):
        for nucleotide in range(0,4):
            matrix[nucleotide].append((count(motifs,nucleotide,i)+1) / (len(motifs)+4))
    return  matrix

def Motifs(dnalist, profile):
    t = len(dnalist)
    k = len(profile[0])
    motifs = []
    for i in range(0, t):
        motifs.append(MostProbkmerinText(dnalist[i], k, profile))
    return motifs

def RandomizedMotifSearchAtom(dnalist, k):
    import random
    n = len(dnalist[0])
    randpos = [random.randint(0, n - k) for i in range(0, len(dnalist))]
    #zip(randpos, dna)=[(poz1,dna1),...,(pozt,dnat)]
    #bestmotifs=[dna1[poz1,poz1+k],...,dnat[pozt,pozt+k]]
    bestmotifs = [x[1][x[0] : (x[0] + k)] for x in zip(randpos, dnalist)]
    motifs = bestmotifs
    while True:
        profile = profileMatrixPseudocounts(motifs,k)
        motifs = Motifs(dnalist, profile)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs

def ProfileRandomlyGeneratedKmer(text, profile, k):
    import random
    L = []
    for i in range(0, len(text) - k + 1):
        L.append(probability(text[i : i + k], profile))
    C = sum(L)
    L = [x / C for x in L]
    r = random.uniform(0, 1)
    s = 0
    for ind, x in enumerate(L):
        s = s + x
        if r < s:
            return text[ind : ind + k]

def GibbsSamplerAtom(dnalist, k, N=1000):
    import random
    t = len(dnalist)
    bestmotifs = RandomizedMotifSearchAtom(dnalist, k)
    motifs = list(bestmotifs)
    for j in range(1, N):
        i = random.randint(0, t - 1)
        #tmp=list(motifs) because tmp.pop() would pop the element from motifs
        tmp = list(motifs)
        tmp.pop(i)
        profile = profileMatrixPseudocounts(tmp,len(tmp[0]))
        motifs[i] = ProfileRandomlyGeneratedKmer(dnalist[i], profile, k)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs

def GibbsSampler(dnalist, k, repeats=20, N=1000):
    bestmotifs = GibbsSamplerAtom(dnalist, k, N)
    for i in range(1, repeats):
        motifs = GibbsSamplerAtom(dnalist, k, N)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs

x='''8 5 100
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA'''
inlines=x.split()
k=int(inlines[0])
t=int(inlines[1])
N=int(inlines[2])
dnalist=list()
for i in range(3,len(inlines)):
    dnalist.append(inlines[i])
result=GibbsSampler(dnalist, k, 20, 1000)
for i in range(0,t):
    print(result[i])

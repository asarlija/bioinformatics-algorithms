"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement GreedyMotifSearch
Rosalind ID: BA2D
URL: http://rosalind.info/problems/ba2d/
"""
def kmer(text,i,k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range(len(text)-L+1):
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

def count(motifs,nucleotide,i):
    """compute count for each nucleotide of i-th column"""
    column=[motif[i] for motif in motifs]
    num=0
    if nucleotide==0:
        num=len([n for n in column if n=='A'])
    if nucleotide==1:
        num=len([n for n in column if n=='C'])
    if nucleotide==2:
        num=len([n for n in column if n=='G'])
    if nucleotide==3:
        num=len([n for n in column if n=='T'])
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

def profileMatrix(motifs,k):
    """ for given set of motifs and k returns profile matrix """
    matrix=[]
    for i in range(0,4):
        matrix.append(list())
    for i in range(0,k):
        for nucleotide in range(0,4):
            matrix[nucleotide].append(count(motifs,nucleotide,i) / len(motifs))
    return  matrix

def GreedyMotifSearch(dnalist,k,t):
    """ for given dna list, k and t returns best motifs"""
    BestMotifs=[kmer(dna,0,k) for dna in dnalist]
    for motif in Lwindows(dnalist[0],k):
        motifs=[motif]
        for i in range(1,t):
            profile=profileMatrix(motifs,k)
            motifs.append(MostProbkmerinText(dnalist[i],k,profile))
        if score(motifs)<score(BestMotifs):
            BestMotifs=motifs
    return BestMotifs

x = '''3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG'''
inlines=x.split()
k=int(inlines[0])
t=int(inlines[1])
dnalist=list()
for i in range(2,len(inlines)):
    dnalist.append(inlines[i])
result=GreedyMotifSearch(dnalist,k,t)
print(result)

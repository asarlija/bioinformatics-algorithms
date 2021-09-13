"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Implement GreedyMotifSearch with Pseudocounts
Rosalind ID: BA2E
URL: http://rosalind.info/problems/ba2e/
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

def GreedyMotifSearchPseudocounts(dnalist, k, t):
    """ for given dna list, k and t returns best motifs"""
    BestMotifs = [kmer(dna,0,k) for dna in dnalist]
    for motif in Lwindows(dnalist[0],k):
        motifs=[motif]
        for i in range(1,t):
            profile=profileMatrixPseudocounts(motifs,k)
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
result=GreedyMotifSearchPseudocounts(dnalist,k,t)
print(result)

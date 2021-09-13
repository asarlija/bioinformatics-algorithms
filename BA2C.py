"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Profile-most Probable k-mer in a String
Rosalind ID: BA2C
URL: http://rosalind.info/problems/ba2c/
"""
def kmer(text, i, k):
    """ substring of text from i-th position for the next k letters """
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
    d=dict()
    for window in Lwindows(text,k):
        d[window]=probability(window,profile)
    listkmers=[key for key,value in d.items() if value==max(d.values())]
    return listkmers[0]

x = '''ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2'''
inlines=x.split('\n')
text=inlines[0]
k=int(inlines[1])
profile=list()
for i in range(2,6):
    profile.append(inlines[i].split())
result=MostProbkmerinText(text,k,profile)
print(result)

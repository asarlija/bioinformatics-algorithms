"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Construct the De Bruijn Graph of a Collection of k-mers
Rosalind ID: BA3E
URL: http://rosalind.info/problems/ba3e/
"""

def suffix(text):
    return text[1:]
def prefix(text):
    return text[:len(text)-1]

def CompositionGraph(patterns):
    L=list()
    for pattern in patterns:
        L.append([prefix(pattern),suffix(pattern)])
    return L

def DeBruijnGraphfromkmersProblem(patterns):
    L=CompositionGraph(patterns)
    RES={}
    for i in range(0,len(L)):
        try:
            RES[L[i][0]].append(L[i][1])
        except KeyError:
            RES[L[i][0]]=[L[i][1]]
    return RES
    
x="""GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG"""
patterns=x.split()
result=DeBruijnGraphfromkmersProblem(patterns)


for key in result.keys():
    print(key,'->',", ".join(result[key]))

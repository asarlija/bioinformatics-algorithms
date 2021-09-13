"""
A solution to a Rosalind bioinformatics problem
Problem Title: Generate the k-mer Composition of a String
Rosalind ID: BA3A
URL: http://rosalind.info/problems/ba3a/
"""

def kmerComposition(text, k):
    """Return all kmers appearing in text sorted in lexografical order"""
    kmerarray=[]
    for i in range(0,len(text) - k + 1):
        kmerarray.append(text[i : (i + k)])
    return sorted(kmerarray)


x="""5
CAATCCAAC"""
inlines=x.split()
k=int(inlines[0])
text=inlines[1]
result=kmerComposition(text, k)
for i in range(0,len(result)):
    print(result[i])


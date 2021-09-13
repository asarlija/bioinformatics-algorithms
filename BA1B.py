"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find the Most Frequent Words in a String
Rosalind ID: BA1B
URL: http://rosalind.info/problems/ba1b/
"""


def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i : (i + k)]


def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return D


def mostfrequentkmers(text, k):
    D=kmersfrequency(text,k)
    maxnum=max(D.values())
    return [key for key,value in D.items() if value==maxnum]

x="""ACGTTGCATGTCGCATGATGCATGAGAGCT
4"""
inlines=x.split("\n")
text=inlines[0]
k=int(inlines[1])
result=mostfrequentkmers(text, k)
resultprint=result[0]
for i in range(1,len(result)):
    resultprint=resultprint+ " "+result[i]
print(resultprint)

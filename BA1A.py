"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Compute the Number of Times a Pattern Appears in a Text
Rosalind ID: BA1A
URL: http://rosalind.info/problems/ba1a/
"""


def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i : (i + k)]


def patterncount(text, pattern):
    """Find a number of time pattern appears in a text"""
    count = 0
    np = len(pattern)
    for i in range(0, len(text) - np + 1):
        if kmer(text, i, np) == pattern:
            count = count + 1
    return count

x="""GCGCG
GCG"""
inlines=x.split("\n")
text=inlines[0]
pattern=inlines[1]
result=patterncount(text,pattern)
print(" ".join(result))

"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find All Approximate Occurrences of a Pattern in a String
Rosalind ID: BA1H
URL: http://rosalind.info/problems/ba1h/

Approximate Pattern Matching Problem
Find all approximate occurrences of a pattern in a string.
Given: Strings Pattern and Text along with an integer d.
Return: All starting positions where Pattern appears as a
substring of Text with at most d mismatches.
"""

def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = text[i : (i + k)]
        try:
            D[tmp].append(i)
        except KeyError:
            D[tmp] = [i]
    return D

def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1

    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist

def ApproximatePatternMatching(text, pattern, d):
    """Find All Approximate Occurrences of a Pattern in a String"""
    D = kmersfrequency(text, len(pattern))
    L = list()
    [L.extend(value) for key, value in D.items() if HammingDistance(key, pattern) <= d]
    return sorted(L)

x="""ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
3"""
inlines=x.split("\n")
pattern=inlines[0]
text=inlines[1]
d=int(inlines[2])
listofpositions=ApproximatePatternMatching(text, pattern, d)
print(sorted(listofpositions))

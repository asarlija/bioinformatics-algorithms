"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find All Occurrences of a Pattern in a String
Rosalind ID: BA1D
URL: http://rosalind.info/problems/ba1d/


Pattern Matching Problem
Find all occurrences of a pattern in a string.
Given: Strings Pattern and Genome.
Return: All starting positions in Genome where Pattern
appears as a substring. Use 0-based indexing.
"""
def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i : (i + k)]


def pattern_occurrences(text, pattern):
    """Find a position of pattern in the text"""
    list_pattern=[]
    np = len(pattern)
    for i in range(0, len(text) - np + 1):
        if kmer(text, i, np) == pattern:
            list_pattern.append(i)
    return list_pattern

x="""ATAT
GATATATGCATATACTT"""
inlines=x.split("\n")
pattern=inlines[0]
text=inlines[1]
result=pattern_occurrences(text, pattern)
print(result)

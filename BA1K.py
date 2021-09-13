"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Generate the Frequency Array of a String
Rosalind ID: BA1K
URL: http://rosalind.info/problems/ba1k
"""
def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def PatternToNumber(pattern):
    result = 0
    k = 0
    for x in pattern[::-1]:
        if x == 'C':
            result = result + 1 * (4 ** k)
        if x == 'G':
            result = result + 2 * (4 ** k)
        if x == 'T':
            result = result + 3 * (4 ** k)
        k = k + 1
    return result


def ComputingFrequencyArray(text,k):
    array=[0]*(4**k)
    for i in range(0,len(text)-k+1):
        pattern=kmer(text, i, k)
        number=PatternToNumber(pattern)
        array[number]+=1
    return array

x="""ACGCGGCTCTGAAA
2"""
inlines=x.split()
text=inlines[0]
k=int(inlines[1])
result=ComputingFrequencyArray(text,k)
print(" ".join([str(x) for x in result])) 

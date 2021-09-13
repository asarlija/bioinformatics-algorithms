"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find a Position in a Genome Minimizing the Skew
Rosalind ID: BA1F
URL: http://rosalind.info/problems/ba1f/

Minimum Skew Problem
Find a position in a genome minimizing the skew.
Given: A DNA string Genome.
Return: All integer(s) i minimizing Skew(Prefixi (Text))
over all values of i (from 0 to |Genome|).
"""

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def skew(text):
    """ the difference between the total number of occurrences of 'G' and 'C' in Genome """
    sk=[0]*(len(text)+1)
    for k in range (1,len(text)+1):
        if kmer(text,0,k)[-1]=='C':
            sk[k]=sk[k-1]-1
        else:
            if kmer(text,0,k)[-1]=='G':
                sk[k]=sk[k-1]+1
            else:
                sk[k]=sk[k-1]
    return sk

def intigersminimizingskew(skew):
    """ finding all intigers minimizing Skew """
    listofindices=list()
    minimumofskew=min(skew)
    for i in range (0,len(skew)):
        if skew[i]==minimumofskew:
            listofindices.append(i)
    return listofindices

text=genome="CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
skew_array=skew(text)
listofindices=intigersminimizingskew(skew_array)
print(listofindices)



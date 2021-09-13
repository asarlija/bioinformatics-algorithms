"""
A solution to a Rosalind bioinformatics problem
Problem Title: Reconstruct a String from its Genome Path
Rosalind ID: BA3B
URL: http://rosalind.info/problems/ba3b/
"""
def string_spelled(genome_path):
    """Find the string spelled by a genome path"""
    result=genome_path[0]
    for i in range(1,len(genome_path)):
        result=result+genome_path[i][-1]
    return result 


x="""ACCGA
CCGAA
CGAAG
GAAGC
AAGCT"""
inlines=x.split()
patterns=list()
for i in range(0,len(inlines)):
    patterns.append(inlines[i])
result=string_spelled(patterns)
print(result)




"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Construct the Overlap Graph of a Collection of k-mers
Rosalind ID: BA3C
URL: http://rosalind.info/problems/ba3c/
"""

def prefix(pattern):
    """substring of pattern without last letter"""
    return pattern[0:len(pattern)-1]

def suffix(pattern):
    """ substring of pattern without first letter"""
    return pattern[1:]

def overlap_graph(kmers):
    """ returns dictionary where key is pattern and values are pattern' """
    dictionary=dict()
    kmers.sort()
    for pattern in kmers:
        dictionary[pattern]=[]
    for pattern in kmers:
        for pattern2 in kmers:
            if suffix(pattern)==prefix(pattern2):
                dictionary[pattern].append(pattern2)
    return dictionary

def graph_print(dictionary):
    for key in dictionary.keys():
        if len(dictionary[key])>0:
            for element in dictionary[key]:
                print(key,'->',element)
x="""ATGCG
GCATG
CATGC
AGGCA
GGCAT"""
inlines=x.split()
kmers=list()
for i in range(0,len(inlines)):
    kmers.append(inlines[i])
result=overlap_graph(kmers)
graph_print(result)




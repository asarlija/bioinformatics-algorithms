"""
A solution to a Rosalind bioinformatics problem
Problem Title: Construct the De Bruijn Graph of a String
Rosalind ID: BA3D
URL: http://rosalind.info/problems/ba3d/
"""

def deBrujinGraph(k, text):
    D = {}
    for i in range(0, len(text) - k + 1):
        first = text[i : (i + k - 1)]
        second = text[(i + 1) : (i + k)]
        if first not in D:
            D[first] = [second]
        else:
            D[first].append(second)
    return D

x="""4
AAGATTCTCTAC"""
inlines=x.split()
k=int(inlines[0])
text=inlines[1]
dictionary_deBrujin= deBrujinGraph(k, text)
result = ""
keys = sorted(dictionary_deBrujin.keys())
for first in keys:
    second = ",".join(sorted(dictionary_deBrujin[first]))
    result = result + f"{first} -> {second}\n"

print(result)
    



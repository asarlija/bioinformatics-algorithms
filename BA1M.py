"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement NumberToPattern
URL: http://rosalind.info/problems/ba1M/
"""

def NumberToPattern(index, k):
    pattern = list()
    D = {0: "A", 1: "C", 2: "G", 3: "T"}
    q = index
    for i in range(0, k):
        r = q % 4
        q = q // 4
        pattern.append(D[r])
    return "".join(pattern[::-1])

x="""45
4"""
inlines=x.split()
index=int(inlines[0])
k=int(inlines[1])
result=NumberToPattern(index, k)
print(result)

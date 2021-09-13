"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement PatternToNumber
URL: http://rosalind.info/problems/ba1l/
"""

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

pattern="AGT"
result=PatternToNumber(pattern)
print(result)

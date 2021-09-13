"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Find the Reverse Complement of a String
Rosalind ID: BA1C
URL: http://rosalind.info/problems/ba1c/
"""
def complement(string):
    """complement of a string"""
    compl=""
    ns=len(string)
    for i in range(0,ns):
        if string[i]=="A":
            compl+="T"
        if string[i]=="T":
            compl+="A"
        if string[i]=="C":
            compl+="G"
        if string[i]=="G":
            compl+="C"
    return compl

def reversed_string(string):
    """ returns reverse of string"""
    return string[::-1]

pattern="AAAACCCGGT"
result=reversed_string(complement(pattern))
print(result)

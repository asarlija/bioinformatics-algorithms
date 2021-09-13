
"""
A solution to a Rosalind bioinformatics problem
Problem Title: Find All Shared k-mers of a Pair of Strings
Rosalind ID: BA6E
URL: http://rosalind.info/problems/ba6e/
"""
def kmer(text,i,k):
    return text[i:(i+k)]

def reversed_complement(text):
    s=""
    for i in range(0,len(text)):
        if text[i]=="A":
            s+="T"
        if text[i]=="T":
            s+="A"
        if text[i]=="C":
            s+="G"
        if text[i]=="G":
            s+="C"
    return s[::-1]

def Sharedkmers(first,second,k):
    S=[]
    for i in range(0,len(first)-k+1):
        for j in range(0,len(second)-k+1):
            if kmer(first,i,k)==kmer(second,j,k):
                S.append([i,j])
            if kmer(first,i,k)==reversed_complement(kmer(second,j,k)):
                S.append([i,j])
    return S

def printSharedkmers(L):
    for i in range(0,len(L)):
        print("("+str(L[i][0])+", "+str(L[i][1])+")")

x="""3
AAACTCATC
TTTCAAATC"""
inlines=x.split()
k=int(inlines[0])
first,second=inlines[1],inlines[2]
result=Sharedkmers(first,second,k)
printSharedkmers(result)
